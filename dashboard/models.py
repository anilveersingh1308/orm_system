from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    state = models.CharField(max_length=20)
    payables = models.IntegerField()

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
    bill_date = models.DateField()
    bill_no = models.CharField(max_length=50)
    bill_reference = models.CharField(max_length=150, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)  # Changed to lowercase
    bill_status = models.CharField(max_length=30)
    bill_due_date = models.DateField(null=True, blank=True)
    bill_amount = models.IntegerField()

    def __str__(self):
        return f"{self.bill_no} - {self.bill_amount}"

class Payments(models.Model):
    pay_date = models.DateField()

    def __str__(self):
        return str(self.pay_date)
