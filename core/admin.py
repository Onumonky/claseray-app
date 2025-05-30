from django.contrib import admin

# Register your models here.
from core import models



@admin.register(models.Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = [
        "bank_name",
        "id",
        "address",
        "status",
    ]



@admin.register(models.AccountBank)
class AccountBankAdmin(admin.ModelAdmin):
    list_display = [
        "account_name",
        "id",
        "bank",
        "currency",
        "status",
    ]



@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        "currency_name",
        "id",
        "shor_name",
        "status",
    ]


@admin.register(models.CategoryProvider)
class CategoryProviderAdmin(admin.ModelAdmin):
    list_display = [
        "category_name",
        "id",
        "status",
    ]


@admin.register(models.Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = [
        "provider_name",
        "id",
        "status",
    ]


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        "payment_name",
        "id",
        "provider",
        "account",
        "timestamp",
        "status",
    ]