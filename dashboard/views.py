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


from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Vendor, Expense, Bill
from .DataArray import APPAREL_VENDOR_LIST, PAYMENT_METHOD_CHOICES, TAX_AND_TAX_GROUP_CHOICES, EXPENSE_ACCOUNT_CHOICES, APPAREL_CUSTOMER_LIST
from .DataArray import APPAREL_MANUFACTURING_ITEM_DETAILS
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

        vendor = Vendor(
            name=name,
            company_name=company_name,
            email=email,
            phone=phone,
            state=state,
            payables=payables
        )
        vendor.save()
        return redirect(reverse('vendors'))
    else:
        return render(request, 'dashboard/new_vendor.html')

def newBill(request):
    if request.method == "POST":
        bill_date = request.POST.get("bill_date")
        bill_no = request.POST.get("bill_no")
        bill_reference = request.POST.get("bill_reference")
        vendor_id = request.POST.get("vendor_id")
        bill_status = request.POST.get("bill_status")
        bill_due_date = request.POST.get("bill_due_date")
        bill_amount = request.POST.get("bill_amount")

        vendor = Vendor.objects.get(id=vendor_id)
        bill = Bill(
            bill_date=bill_date,
            bill_no=bill_no,
            bill_reference=bill_reference,
            vendor=vendor,
            bill_status=bill_status,
            bill_due_date=bill_due_date,
            bill_amount=bill_amount
        )
        bill.save()
        return redirect(reverse('bills'))
    else:
        vendors = Vendor.objects.all()
        context = {
            "vendors": vendors,
            "customer":APPAREL_CUSTOMER_LIST,
            "payment_terms": PAYMENT_METHOD_CHOICES,
            "tax_choices": TAX_AND_TAX_GROUP_CHOICES,
            "expense_account_choices": EXPENSE_ACCOUNT_CHOICES,
            "apparel_items_json": json.dumps(APPAREL_MANUFACTURING_ITEM_DETAILS)
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
