from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .data_array import bills_data, expenses_data, vendors_data


context = {
    "bills": bills_data,
    "expenses": expenses_data,
    "vendors": vendors_data,
    "total_payable": "₹37,85,349.54",
    "due_today": "₹0.00",
    "due_30_days": "₹0.00",
    "overdue_total": "₹37,85,349.54"
}


def home(request):
    return render(request, 'dashboard/base.html')

def vendors(request):
    return render(request, 'dashboard/base.html', context)

def expenses(request):
    return render(request, 'dashboard/base.html', context)

def bills(request):
    # return render(request, 'bills.html', context)
    return render(request, 'dashboard/base.html', context)


# AJAX content loading
def ajax_home(request):
    html = render_to_string('dashboard/home.html')
    return JsonResponse({'html': html})

def ajax_vendors(request):
    html = render_to_string('dashboard/vendors.html', context)  # Pass vendors_data
    return JsonResponse({'html': html})

def ajax_expenses(request):
    html = render_to_string('dashboard/expenses.html', context)  # Pass expenses_data
    return JsonResponse({'html': html})

def ajax_bills(request):
    html = render_to_string('dashboard/bills.html', context)
    return JsonResponse({'html': html})
