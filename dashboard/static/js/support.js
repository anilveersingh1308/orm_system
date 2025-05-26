document.addEventListener("DOMContentLoaded", function () {
    // Get references
    const addItemButton = document.querySelector('.add-item');
    const itemTableBody = document.querySelector('#itemTable tbody');

    // Get the account select HTML from the template (rendered by Django)
    const accountSelectHTML = document.querySelector('select[name="account[]"]')?.outerHTML || '';
    // Get the tax select HTML from the template (rendered by Django)
    const taxSelectHTML = document.querySelector('select[name="tax[]"]')?.outerHTML || '';

    // Item data for autocomplete and autofill (from Django context)
    const itemData = typeof apparelItemsData !== 'undefined' ? apparelItemsData : [];
    document.querySelectorAll('#itemTable tbody tr').forEach(function(row) {
        const input = row.querySelector('input[placeholder="Type or click to select item"]');
        if (input) {
            attachAutocomplete(input);
        }
    });
    function isRowEmpty(row) {
        // Check if all input/select fields in the row are empty (ignoring buttons)
        const inputs = row.querySelectorAll('input, select');
        for (let input of inputs) {
            if (input.type === 'button' || input.type === 'submit' || input.type === 'reset') { continue; }
            // Only check the item details input for emptiness
            if (input.classList.contains('item-autocomplete')) {
                if (input.value && input.value.trim() !== '') {
                    return false;
                }
            }
        }
        return true;
    }

    function createNewRow(e) {
        if (e) { e.preventDefault(); }
        // Prevent adding a new row if the last row's item details input is empty
        const lastRow = itemTableBody.querySelector('tr:last-child');
        if (lastRow && isRowEmpty(lastRow)) {
            lastRow.querySelector('.item-autocomplete')?.focus();
            return;
        }
        const row = document.createElement('tr');
        row.innerHTML = `
        <td class="item-autocomplete-cell">
            <input type="text" class="form-control item-autocomplete" placeholder="Type or click to select item" autocomplete="off">
            <div class="autocomplete-list" style="position:relative;"></div>
        </td>
        <td>${accountSelectHTML}</td>
        <td><input type="number" class="form-control" value="1.00" name="quantity[]"></td>
        <td><input type="number" name="rate[]" class="form-control" value="0"></td>
        <td>${taxSelectHTML}</td>
        <td><select class="form-select"><option>Regular/RCM</option></select></td>
        <td><input type="number" class="form-control" name="amount[]" value="0" readonly tabindex="-1"></td>
        <td><button type="button" class="btn btn-danger btn-sm delete-row">X</button></td>
        `;
        itemTableBody.appendChild(row);
        attachAutocomplete(row.querySelector('.item-autocomplete'));
        attachAmountListeners(row); // Attach amount listeners to the new row
        updateAllAmounts(); // Immediately update the amount for the new row
    }

    // Attach autocomplete to all item input fields
    function attachAutocomplete(input) {
        const cell = input.closest('.item-autocomplete-cell');
        if (!cell) { return; } // Prevent error if cell is not found
        const dropdown = cell.querySelector('.autocomplete-list');
        if (!dropdown) { return; } // Prevent error if dropdown is not found
        input.addEventListener('input', function () {
            const val = input.value.trim().toLowerCase();
            dropdown.innerHTML = '';
            if (!val) { return; }
            const matches = itemData.filter(item => item.name.toLowerCase().startsWith(val));
            if (matches.length === 0) { return; }
            const list = document.createElement('ul');
            list.className = 'list-group position-absolute w-100';
            matches.forEach(item => {
                const li = document.createElement('li');
                li.className = 'list-group-item list-group-item-action';
                li.textContent = item.name;
                li.addEventListener('mousedown', function (e) {
                    e.preventDefault();
                    input.value = item.name;
                    // Autofill columns
                    const row = input.closest('tr');
                    // Account
                    const accSelect = row.querySelector('select[name="account[]"]');
                    if (accSelect) { accSelect.value = item.account; }
                    // Quantity
                    const qtyInput = row.children[2]?.querySelector('input');
                    if (qtyInput) { qtyInput.value = 1; }
                    // Rate
                    const rateInput = row.children[3]?.querySelector('input');
                    if (rateInput) { rateInput.value = item.cost; }
                    // Tax
                    const taxSelect = row.querySelector('select[name="tax[]"]');
                    if (taxSelect) {
                        // Try to match IGST or GST
                        let taxVal = '';
                        if (item.tax_rates && item.tax_rates.igst) {
                            taxVal = 'igst_' + item.tax_rates.igst;
                        } else if (item.tax_rates && item.tax_rates.gst) {
                            taxVal = 'gst_' + item.tax_rates.gst;
                        }
                        taxSelect.value = taxVal;
                    }
                    // Remove dropdown
                    if (dropdown) { dropdown.innerHTML = ''; }
                });
                list.appendChild(li);
            });
            dropdown.appendChild(list);
        });
        // Hide dropdown on blur
        input.addEventListener('blur', function () {
            setTimeout(() => { if (dropdown) { dropdown.innerHTML = ''; } }, 150);
        });
    }

    // Calculate and update amount fields based on rate and quantity
    function updateAllAmounts() {
        // For each row in the item table
        document.querySelectorAll('#itemTable tbody tr').forEach(function(row) {
            const qtyInput = row.querySelector('input[name="quantity[]"]');
            const rateInput = row.querySelector('input[name="rate[]"]');
            const amountInput = row.querySelector('input[name="amount[]"]');
            if (qtyInput && rateInput && amountInput) {
                const qty = parseFloat(qtyInput.value) || 0;
                const rate = parseFloat(rateInput.value) || 0;
                amountInput.value = (qty * rate).toFixed(2);
            }
        });
    }

    // Attach event listeners to update amount on input change
    function attachAmountListeners(row) {
        const qtyInput = row.querySelector('input[name="quantity[]"]');
        const rateInput = row.querySelector('input[name="rate[]"]');
        if (qtyInput) {
            qtyInput.addEventListener('input', updateAllAmounts);
        }
        if (rateInput) {
            rateInput.addEventListener('input', updateAllAmounts);
        }
    }

    // Attach autocomplete to all initial item fields (including the first row)
    document.querySelectorAll('#itemTable tbody tr').forEach(function(row) {
        const input = row.querySelector('input[placeholder="Type or click to select item"]');
        if (input) {
            attachAutocomplete(input);
        }
    });
    document.querySelectorAll('#itemTable tbody tr').forEach(attachAmountListeners); // Attach listeners to all initial rows

    if (addItemButton && itemTableBody) {
        addItemButton.addEventListener('click', createNewRow);
        itemTableBody.addEventListener('click', function (e) {
            if (e.target && e.target.classList.contains('delete-row')) {
                e.target.closest('tr').remove();
            }
        });
    }

    // Prevent Enter key from triggering add row or deleting row in the item table
    itemTableBody.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') {
            // Only prevent default if the event target is an input or select inside the table
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') {
                e.preventDefault();
                // Optionally, move to next input in the row or do nothing
            }
        }
    }, true);

    // Prevent Enter key from submitting the form if not all required fields are filled
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' && e.target.tagName !== 'TEXTAREA') {
                // Only prevent default if the event target is inside the item table or is a required field
                const inTable = e.target.closest('.item-table');
                const isRequired = e.target.hasAttribute('required');
                if (inTable || isRequired) {
                    // Check required fields
                    const requiredFields = form.querySelectorAll('[required], .form-control[required], select[required]');
                    let allFilled = true;
                    requiredFields.forEach(field => {
                        if (!field.value || field.value.trim() === '') {
                            allFilled = false;
                        }
                    });
                    if (!allFilled) {
                        e.preventDefault();
                    }
                } else {
                    // Prevent Enter from submitting the form in any input/select except textarea
                    e.preventDefault();
                }
            }
        });
    }

    updateAllAmounts(); // Optionally, call this on page load to initialize
});