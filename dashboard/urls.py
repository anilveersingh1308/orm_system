from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vendors/', views.vendors, name='vendors'),
    path('expenses/', views.expenses, name='expenses'),
    path('bills/', views.bills, name='bills'),  # Add this line
    path('bills/<int:bill_id>/', views.bill_display, name='bill_display'),  # Add this line
    path('vendors/new-vendor/', views.newVendor, name='new_vendor'),  # Add this line
    path('bills/new-bill/', views.newBill, name='new_bill'),  # Add this line
    path('expenses/new-expense/', views.newExpense, name='new_expense'),  # Add this line
    path('bills/<int:bill_id>/edit/', views.bill_edit, name='bill_edit'),  # Edit bill page
    path('vendors/<int:vendor_id>/', views.vendor_detail, name='vendor_detail'),  # Vendor detail page
    
    # AJAX Views
    # path('ajax/load/home/', views.ajax_home, name='ajax_home'),
    # path('ajax/load/vendors/', views.ajax_vendors, name='ajax_vendors'),
    # path('ajax/load/expenses/', views.ajax_expenses, name='ajax_expenses'),
    # path('ajax/load/bills/', views.ajax_bills, name='ajax_bills'),
]
