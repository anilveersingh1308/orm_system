from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    state = models.CharField(max_length=20)
    payables = models.IntegerField()
    # New fields for full vendor details
    address = models.TextField(null=True, blank=True)
    primary_contact = models.CharField(max_length=255, null=True, blank=True)
    gstin = models.CharField(max_length=30, null=True, blank=True)
    # Billing Address
    billing_address = models.TextField(null=True, blank=True)
    billing_city = models.CharField(max_length=100, null=True, blank=True)
    billing_state = models.CharField(max_length=100, null=True, blank=True)
    billing_zip = models.CharField(max_length=20, null=True, blank=True)
    # Shipping Address
    shipping_address = models.TextField(null=True, blank=True)
    shipping_city = models.CharField(max_length=100, null=True, blank=True)
    shipping_state = models.CharField(max_length=100, null=True, blank=True)
    shipping_zip = models.CharField(max_length=20, null=True, blank=True)
    # Bank Details
    bank_account_number = models.CharField(max_length=50, null=True, blank=True)
    bank_ifsc = models.CharField(max_length=20, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    exp_date = models.DateField()
    account = models.CharField(max_length=50)
    exp_reference = models.CharField(max_length=150)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)  # Changed to lowercase
    customer = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    exp_amount = models.IntegerField()

    def __str__(self):
        return f"{self.exp_reference} - {self.exp_amount}"

class Bill(models.Model):
    bill_no = models.CharField(max_length=50)
    bill_reference = models.CharField(max_length=150, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)  # Changed to lowercase
    bill_status = models.CharField(max_length=30)
    bill_date = models.DateField()
    bill_due_date = models.DateField(null=True, blank=True)
    payment_terms = models.CharField(max_length=100, null=True, blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    adjustment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.bill_no} - {self.total_amount}"

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='items')
    item_details = models.CharField(max_length=255)
    account = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.CharField(max_length=50)
    customer = models.CharField(max_length=255, null=True, blank=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.item_details} - {self.amount}"

class Payments(models.Model):
    pay_date = models.DateField()

    def __str__(self):
        return str(self.pay_date)
