from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vendors/', views.vendors, name='vendors'),
    path('expenses/', views.expenses, name='expenses'),
    path('bills/', views.bills, name='bills'),  # Add this line
    
    # AJAX Views
    path('ajax/load/home/', views.ajax_home, name='ajax_home'),
    path('ajax/load/vendors/', views.ajax_vendors, name='ajax_vendors'),
    path('ajax/load/expenses/', views.ajax_expenses, name='ajax_expenses'),
    path('ajax/load/bills/', views.ajax_bills, name='ajax_bills'),
]
