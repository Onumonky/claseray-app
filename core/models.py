from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bank(models.Model):
    bank_name = models.CharField(max_length=32, default="Generic Bank Name")
    address = models.CharField(max_length=32, default="Generic Bank Address")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.bank_name
    



class Currency(models.Model):
    currency_name = models.CharField(max_length=16, default="Genercurren Name")
    shor_name = models.CharField(max_length=3, default="GC")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.currency_name
    


class AccountBank(models.Model):
    account_name = models.CharField(max_length=16, default="Generic Account")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.account_name
    



class CategoryProvider(models.Model):
    category_name = models.CharField(max_length=16, default="Generic Category")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
    


class Provider(models.Model):
    provider_name = models.CharField(max_length=32, default="Generic Provider Name")
    category = models.ForeignKey(CategoryProvider, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.provider_name



class Payment(models.Model):
    payment_name = models.CharField(max_length=32, default="Generic Payment Name")
    account = models.ForeignKey(AccountBank, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.payment_name


"""

Cuentas banco
    Bancos
    Divisas

Proveedores
    Categorias

Pagos
    Cuentas
    Proveedores
"""