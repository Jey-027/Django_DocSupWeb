from django import forms
from .models import documento
import time

class documentoForm(forms.ModelForm):
    class Meta:
        model = documento
        fields = [
        #"Date_process"
        "id"
        ,"id_supplier_vendor"
        ,"name_supplier_vendor"
        ,"id_supplier_invoice"
        ,"net_amount"
        ,"payment_date"
        ,"user_process"
    ]



