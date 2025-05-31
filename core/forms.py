from django import forms

from core import models


class CreateBankForm(forms.ModelForm):
    class Meta:
        model = models.Bank
        fields = [
            "bank_name",
            "address",
            "status",
        ]
        widgets = {
            "bank_name": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Escribe el nombre del Banco!"}),
            "address": forms.TextInput(attrs={"type": "text", "class": "form-control", "placeholder": "Escribe la direccion del Banco!"}),
        }