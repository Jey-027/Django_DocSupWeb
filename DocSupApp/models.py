from datetime import date
from django.db import models

# Create your models here.
class proveedor(models.Model):
    id_supplier=models.CharField(max_length=20, primary_key=True)
    name=models.CharField(max_length=100)
    supplier_tax_code=models.CharField(max_length=10)
    city_id=models.CharField(max_length=10)
    city_name=models.CharField(max_length=40)
    email=models.CharField(max_length=50)
    nit=models.CharField(max_length=20)
    supplier_tax_description=models.CharField(max_length=70)
    Type_of_tax_number=models.CharField(max_length=70)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=10)
    est_fed_prov=models.CharField(max_length=10)
    name_est_fed_prov=models.CharField(max_length=40)
    currency_type=models.CharField(max_length=10)

    normal_pagination = True
    # values_for_page = 5
    

    def get_absolute_url(self):
        return "/proveedor"

    def __str__(self):
        return f"{self.name}"


class documento(models.Model):
    personType_choices = [
        ("2", "Persona Natural"),
        ("1", "Persona Juridica"),
    ]

    id = models.AutoField(primary_key=True) 
    id_supplier_vendor = models.CharField(max_length=20)
    name_supplier_vendor = models.CharField(max_length=100)
    suplier_tax_code = models.CharField(max_length=10)
    city_id = models.CharField(max_length=10)
    city_name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    Nit = models.CharField(max_length=20)
    type_of_tax_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=10)
    est_fed_prov = models.CharField(max_length=10)
    name_est_fed_prov = models.CharField(max_length=40)
    currency_type = models.CharField(max_length=20)
    supplier_id_Customer = models.CharField(max_length=20)
    name_supplier_customer = models.CharField(max_length=100)
    id_supplier_invoice = models.CharField(max_length=55)
    date_Invoice = models.DateField(date)
    idItem = models.CharField(max_length=40)
    item_description = models.CharField(max_length=100)
    zSupplierID = models.CharField(max_length=20)
    zSupplierName = models.CharField(max_length=100)
    net_amount = models.CharField(max_length=20)
    tax_amount = models.CharField(max_length=20)
    gross_amount = models.CharField(max_length=20)
    percent_RTE = models.CharField(max_length=20)
    percent_IVA = models.CharField(max_length=20)
    percent_ICA = models.CharField(max_length=20)
    amount_RTE = models.CharField(max_length=20)
    amount_IVA = models.CharField(max_length=20)
    amount_ICA = models.CharField(max_length=20)
    Value_RTE = models.CharField(max_length=30)
    total_retenciones = models.CharField(max_length=30)
    tipo_persona = models.TextField(null=True, choices=personType_choices)
    status = models.TextField(null=True)  
    Date_process = models.DateTimeField(null=True)
    user_process = models.CharField(max_length=30, null=True)
    payment_date = models.DateField(null=True)
    num_documento = models.CharField(max_length=100, null=True)

    # normal_pagination = True
    # values_for_page = 20

    def get_abosulte_url(self):
        return "/documento"
    
    def __str__(self):
        return f"{self.id, self.suplier_tax_code, self.Nit, self.type_of_tax_number, self.date_Invoice, self.item_description, self.tax_amount, self.net_amount, self.payment_date}"


class properties(models.Model):
    id = models.AutoField(primary_key=True)
    Num_resolution = models.IntegerField()
    path_file = models.CharField(max_length=100, null=True)
    name_file = models.CharField(max_length=100, null=True)
    autorization = models.CharField(max_length=100, null=True)
    start_date_res = models.DateField(null=True)
    end_date_res = models.DateField(null=True)
    prefijo_res = models.CharField(max_length=10, null=True)
    initial_range_res = models.IntegerField(null=True)
    end_range_res = models.IntegerField(null=True)



    def __str__(self):
        return f"{self.Num_resolution}"