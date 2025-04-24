from django.contrib import admin
from .models import Vendor, Expense, Bill, Payments

# Register your models here.

admin.site.register(Vendor)
admin.site.register(Expense)
admin.site.register(Bill)
admin.site.register(Payments)
