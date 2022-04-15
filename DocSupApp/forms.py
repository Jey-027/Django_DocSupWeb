from django import forms
from .models import documento


class documentoForm(forms.ModelForm):
    class Meta:
        model = documento
        
        fields = [
        "id"
        ,"id_supplier_vendor"
        ,"name_supplier_vendor"
        ,"id_supplier_invoice"
        ,"item_description"
        ,"net_amount"
        ,"payment_date"
        ,"tipo_persona" 
        ]

        # labels = {
        #     "payment_date": "Payment Date (YYYY-MM-DD)"
        # }

        widgets = {
            "payment_date" : forms.SelectDateWidget
        }