# from django.shortcuts import render
# from django.http import JsonResponse
# from django.template.loader import render_to_string
# from .data_array import bills_data, expenses_data, vendors_data


# context = {
#     "bills": bills_data,
#     "expenses": expenses_data,
#     "vendors": vendors_data,
#     "total_payable": "₹37,85,349.54",
#     "due_today": "₹0.00",
#     "due_30_days": "₹0.00",
#     "overdue_total": "₹37,85,349.54"
# }


# def home(request):
#     return render(request, 'dashboard/home.html')

# def vendors(request):
#     return render(request, 'dashboard/vendors.html', context)

# def expenses(request):
#     return render(request, 'dashboard/expenses.html', context)

# def bills(request):
#     return render(request, 'dashboard/bills.html', context)
#     # return render(request, 'dashboard/base.html', context)


# # # AJAX content loading
# # def ajax_home(request):
# #     html = render_to_string('dashboard/home.html')
# #     return JsonResponse({'html': html})

# # def ajax_vendors(request):
# #     html = render_to_string('dashboard/vendors.html', context)  # Pass vendors_data
# #     return JsonResponse({'html': html})

# # def ajax_expenses(request):
# #     html = render_to_string('dashboard/expenses.html', context)  # Pass expenses_data
# #     return JsonResponse({'html': html})

# # def ajax_bills(request):
# #     html = render_to_string('dashboard/bills.html', context)
# #     return JsonResponse({'html': html})


from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Vendor, Expense, Bill, BillItem
from .DataArray import APPAREL_VENDOR_LIST, PAYMENT_METHOD_CHOICES, TAX_AND_TAX_GROUP_CHOICES, EXPENSE_ACCOUNT_CHOICES, APPAREL_CUSTOMER_LIST
from .DataArray import APPAREL_MANUFACTURING_ITEM_DETAILS
from django.utils import timezone
import json

def home(request):
    return render(request, 'dashboard/home.html')

def vendors(request):
    vendors = Vendor.objects.all()
    context = {"vendors": vendors}
    return render(request, 'dashboard/vendors.html', context)

def expenses(request):
    expenses = Expense.objects.all()
    context = {"expenses": expenses}
    return render(request, 'dashboard/expenses.html', context)

def bills(request):
    bills = Bill.objects.all()
    context = {"bills": bills}
    return render(request, 'dashboard/bills.html', context)

def newVendor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        company_name = request.POST.get("company_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        state = request.POST.get("state")
        payables = request.POST.get("payables")
        # Primary Contact
        salutation = request.POST.get("salutation")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        primary_contact = " ".join(filter(None, [salutation, first_name, last_name])).strip()
        # GSTIN
        gstin = request.POST.get("gstin")
        # Billing Address
        billing_address1 = request.POST.get("billing_address1")
        billing_address2 = request.POST.get("billing_address2")
        billing_address = (billing_address1 or "") + (", " + billing_address2 if billing_address2 else "")
        billing_city = request.POST.get("billing_city")
        billing_state = request.POST.get("billing_state")
        billing_zip = request.POST.get("billing_pincode")
        # Shipping Address
        shipping_address1 = request.POST.get("shipping_address1")
        shipping_address2 = request.POST.get("shipping_address2")
        shipping_address = (shipping_address1 or "") + (", " + shipping_address2 if shipping_address2 else "")
        shipping_city = request.POST.get("shipping_city")
        shipping_state = request.POST.get("shipping_state")
        shipping_zip = request.POST.get("shipping_pincode")
        # Bank Details
        bank_account_number = request.POST.get("bank_account_number")
        bank_ifsc = request.POST.get("bank_ifsc")
        bank_name = request.POST.get("bank_name")
        # Optional: address (general)
        address = billing_address
        vendor = Vendor(
            name=name,
            company_name=company_name,
            email=email,
            phone=phone,
            state=state,
            payables=payables,
            primary_contact=primary_contact,
            gstin=gstin,
            billing_address=billing_address,
            billing_city=billing_city,
            billing_state=billing_state,
            billing_zip=billing_zip,
            shipping_address=shipping_address,
            shipping_city=shipping_city,
            shipping_state=shipping_state,
            shipping_zip=shipping_zip,
            bank_account_number=bank_account_number,
            bank_ifsc=bank_ifsc,
            bank_name=bank_name,
            address=address
        )
        vendor.save()
        return redirect(reverse('vendors'))
    else:
        return render(request, 'dashboard/new_vendor.html')

def newBill(request):
    if request.method == "POST":
        bill_no = request.POST.get("bill_no")
        bill_reference = request.POST.get("bill_reference")
        vendor_id = request.POST.get("vendor_id")
        bill_status = "Open" if "save_open" in request.POST else "Draft"
        bill_date = request.POST.get("bill_date")
        bill_due_date = request.POST.get("bill_due_date")
        payment_terms = request.POST.get("payment_terms")
        discount = request.POST.get("discount") or 0
        total_tax_amount = request.POST.get("totalTaxAmount") or 0
        adjustment = request.POST.get("adjustment") or 0
        total_amount = request.POST.get("totalAmount") or 0
        notes = request.POST.get("notes")
        vendor = Vendor.objects.get(id=vendor_id)
        bill = Bill.objects.create(
            bill_no=bill_no,
            bill_reference=bill_reference,
            vendor=vendor,
            bill_status=bill_status,
            bill_date=bill_date,
            bill_due_date=bill_due_date,
            payment_terms=payment_terms,
            discount=discount,
            total_tax_amount=total_tax_amount,
            adjustment=adjustment,
            total_amount=total_amount,
            notes=notes
        )
        item_details = request.POST.getlist('item_details[]')
        accounts = request.POST.getlist('account[]')
        quantities = request.POST.getlist('quantity[]')
        rates = request.POST.getlist('rate[]')
        taxes = request.POST.getlist('tax[]')
        customers = request.POST.getlist('customer[]')
        tax_amounts = request.POST.getlist('taxAmount[]')
        amounts = request.POST.getlist('amount[]')
        for i in range(len(item_details)):
            BillItem.objects.create(
                bill=bill,
                item_details=item_details[i],
                account=accounts[i],
                quantity=quantities[i],
                rate=rates[i],
                tax=taxes[i],
                customer=customers[i],
                tax_amount=tax_amounts[i],
                amount=amounts[i]
            )
        return redirect(reverse('bills'))
    else:
        vendors = Vendor.objects.all().distinct()
        from datetime import date
        context = {
            "vendors": vendors,
            "customers": APPAREL_CUSTOMER_LIST,
            "payment_terms": PAYMENT_METHOD_CHOICES,
            "tax_choices": TAX_AND_TAX_GROUP_CHOICES,
            "expense_account_choices": EXPENSE_ACCOUNT_CHOICES,
            "apparel_items_json": json.dumps(APPAREL_MANUFACTURING_ITEM_DETAILS),
            "today": date.today(),
        }
        return render(request, 'dashboard/new_bill.html', context)

def newExpense(request):
    if request.method == "POST":
        exp_date = request.POST.get("exp_date")
        account = request.POST.get("account")
        exp_reference = request.POST.get("exp_reference")
        vendor_id = request.POST.get("vendor_id")
        customer = request.POST.get("customer")
        status = request.POST.get("status")
        exp_amount = request.POST.get("exp_amount")

        vendor = Vendor.objects.get(id=vendor_id)
        expense = Expense(
            exp_date=exp_date,
            account=account,
            exp_reference=exp_reference,
            vendor=vendor,
            customer=customer,
            status=status,
            exp_amount=exp_amount
        )
        expense.save()
        return redirect(reverse('expenses'))
    else:
        
        return render(request, 'dashboard/new_expense.html')

def bill_display(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    items = bill.items.all()
    return render(request, 'dashboard/bill_display.html', {
        'bill': bill,
        'items': items,
    })

def bill_edit(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    if request.method == "POST":
        bill_no = request.POST.get("bill_no", bill.bill_no)
        bill_reference = request.POST.get("bill_reference", bill.bill_reference)
        vendor_id = request.POST.get("vendor_id", bill.vendor.id if bill.vendor else None)
        bill_date = request.POST.get("bill_date", bill.bill_date)
        bill_due_date = request.POST.get("bill_due_date", bill.bill_due_date)
        payment_terms = request.POST.get("payment_terms", bill.payment_terms)
        discount = request.POST.get("discount", bill.discount)
        notes = request.POST.get("notes", bill.notes)
        total_tax_amount = request.POST.get("totalTaxAmount", bill.total_tax_amount)
        adjustment = request.POST.get("adjustment", bill.adjustment)
        total_amount = request.POST.get("totalAmount", bill.total_amount)
        vendor = Vendor.objects.get(id=vendor_id) if vendor_id else bill.vendor
        bill.bill_no = bill_no
        bill.bill_reference = bill_reference
        bill.vendor = vendor
        bill.bill_date = bill_date
        bill.bill_due_date = bill_due_date
        bill.payment_terms = payment_terms
        bill.discount = discount
        bill.notes = notes
        bill.total_tax_amount = total_tax_amount
        bill.adjustment = adjustment
        bill.total_amount = total_amount
        bill.save()
        # Remove all old items and add all new/updated items
        bill.items.all().delete()
        item_details = request.POST.getlist('item_details[]')
        accounts = request.POST.getlist('account[]')
        quantities = request.POST.getlist('quantity[]')
        rates = request.POST.getlist('rate[]')
        taxes = request.POST.getlist('tax[]')
        customers = request.POST.getlist('customer[]')
        tax_amounts = request.POST.getlist('taxAmount[]')
        amounts = request.POST.getlist('amount[]')
        for i in range(len(item_details)):
            BillItem.objects.create(
                bill=bill,
                item_details=item_details[i],
                account=accounts[i],
                quantity=quantities[i],
                rate=rates[i],
                tax=taxes[i],
                customer=customers[i],
                tax_amount=tax_amounts[i],
                amount=amounts[i]
            )
        return redirect(reverse('bill_display', args=[bill.id]))
    else:
        vendors = Vendor.objects.all().distinct()
        from datetime import date
        context = {
            "bill": bill,
            "items": bill.items.all(),
            "vendors": vendors,
            "customers": APPAREL_CUSTOMER_LIST,
            "payment_terms": PAYMENT_METHOD_CHOICES,
            "tax_choices": TAX_AND_TAX_GROUP_CHOICES,
            "expense_account_choices": EXPENSE_ACCOUNT_CHOICES,
            "apparel_items_json": json.dumps(APPAREL_MANUFACTURING_ITEM_DETAILS),
            "today": bill.bill_date,
        }
        return render(request, 'dashboard/bill_edit.html', context)

def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    return render(request, 'dashboard/vendor_detail.html', {'vendor': vendor})
