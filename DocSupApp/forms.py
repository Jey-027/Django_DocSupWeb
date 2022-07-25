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

        widgets = {
            "payment_date" : forms.SelectDateWidget
        }

class documentFormUsd(forms.ModelForm):
    class Meta:
        model = documento

        fields = [
        "id"
        ,"id_supplier_vendor"
        ,"name_supplier_vendor"
        ,"id_supplier_invoice"
        ,"city_name"
        ,"item_description"
        ,"net_amount"
        ,"tasa_cambio"
        ,"fecha_tasa_cambio"
        ,"payment_date"
        ,"tipo_persona" 
        ]

        widgets = {
            "payment_date" : forms.SelectDateWidget,
            "fecha_tasa_cambio": forms.SelectDateWidget
        }
        

class noFileForm(forms.ModelForm):
    class Meta:
        model = documento
        
        fields = [
        "id"
        ,"id_supplier_vendor"
        ,"name_supplier_vendor"
        ,"id_supplier_invoice"
        ,"item_description"
        ,"net_amount"
        ]

class notaCredito(forms.ModelForm):
    class Meta:
        model = documento

        fields = [
            "id"
            ,"id_supplier_vendor"
            ,"name_supplier_vendor"
            ,"id_supplier_invoice"
            ,"item_description"
            ,"net_amount"
            ,"motivo"
        ]
