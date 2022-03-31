from django.db import models

# Create your models here.
class proveedor(models.Model):
    id_supplier=models.CharField(max_length=20, primary_key=True)
    name=models.CharField(max_length=100)
    supplier_tax_code=models.CharField(max_length=100)
    city_id=models.CharField(max_length=10)
    city_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    nit=models.CharField(max_length=20)
    supplier_tax_description=models.CharField(max_length=70)
    Type_of_tax_number=models.CharField(max_length=70)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=10)
    est_fed_prov=models.CharField(max_length=10)
    name_est_fed_prov=models.CharField(max_length=40)
    currency_type=models.CharField(max_length=10)

    def get_absolute_url(self):
        return "/proveedor"

    def __str__(self):
        return f"{self.name}"

class det_fact(models.Model):
    id_supplier=models.CharField(max_length=10)
    name_supplier=models.CharField(max_length=70)
    id_supplier_invoice=models.CharField(max_length=50)
    date_Invoice=models.DateTimeField()
    zPaymentMethod=models.CharField(max_length=40)
    idItem=models.CharField(max_length=10)
    item_description=models.CharField(max_length=100)
    zSupplierName=models.CharField(max_length=100)
    zSupplierID=models.CharField(max_length=10)
    Business_transaction_document_id=models.CharField(max_length=30)
    net_amount=models.CharField(max_length=20)
    tax_amount=models.CharField(max_length=20)
    gross_amount=models.CharField(max_length=20)
    percent_RTE=models.CharField(max_length=20)
    percent_IVA=models.CharField(max_length=20)
    percent_ICA=models.CharField(max_length=20)
    amount_RTE=models.CharField(max_length=20)
    amount_IVA=models.CharField(max_length=20)
    amount_ICA=models.CharField(max_length=20)
    Value_RTE=models.CharField(max_length=20)
    total_retenciones=models.CharField(max_length=20)

    def get_abosulte_url(self):
        return "/det_fact"
    
    def __str__(self):
        return f"{self.name}"