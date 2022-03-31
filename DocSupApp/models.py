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

