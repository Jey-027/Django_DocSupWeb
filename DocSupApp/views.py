from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from .models import documento, proveedor, documento
from django.urls import reverse_lazy
import time
# Create your views here.


#@login_required
def home(request):
    context = {"name": request.user.username}
    return render(request, "DocSupApp/home.html", context)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class vendorList(ListView):
    model = proveedor

class VendorCreate(CreateView):
    model = proveedor
    template_name = "DocSupApp/proveedor_create.html"
    fields = [
    "id_supplier"
    ,"name"
    ,"supplier_tax_code"
    ,"city_id"
    ,"city_name"
    ,"email"
    ,"nit"
    ,"supplier_tax_description"
    ,"Type_of_tax_number"
    ,"address"
    ,"country"
    ,"est_fed_prov"
    ,"name_est_fed_prov"
    ,"currency_type"
    ]
    success_url = "/vendor/list"

class VendorUpdate(UpdateView):
    model = proveedor
    template_name = "DocSupApp/proveedor_update.html"
    fields = [
        "id_supplier"
        ,"name"
        ,"supplier_tax_code"
        ,"city_id"
        ,"city_name"
        ,"email"
        ,"nit"
        ,"supplier_tax_description"
        ,"Type_of_tax_number"
        ,"address"
        ,"country"
        ,"est_fed_prov"
        ,"name_est_fed_prov"
        ,"currency_type"
    ]
    success_url = "/vendor/list"

class DetFactList(ListView):
    model = documento

class DetFactUpdate(UpdateView):
    model = documento
    template_name = "DocSupApp/Genera_file.html"
    fields = [
        # "Date_process"
        # ,"id"
        "id_supplier_vendor"
        ,"name_supplier_vendor"
        ,"id_supplier_invoice"
        ,"zSupplierID"
        ,"net_amount"
        #,"status" 
    ]








#     # def documento(self):
#     f = open("C:/load/txt/pruebaDjangofile21.txt" ,"w+")
#     f.write("ENC,DS,DIAN 2.1: Documento soporte en adquisiciones efectuadas a no obligados a facturar.,DME1503," + time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime()) +"-05:00," + "05,COP,1,2,10,UBL 2.1\n")
#     f.write("CUD,123456789ASD0987654321\n")
#     f.write("EMI,1,,11001,Bogotá D.C.,110111,Bogotá,11,CRA 72 80-94 OF 902 CTRO EMP. TITAN PLAZA,CO,Colombia,,Black & Decker de Colombia S.A.S,935462718,1,31 \n")
  
#     f.close()

#     success_url = "/facturas/list"

# # class CreateFile():
# #     template_name = 'DocSupAp/enviar_file.html'
    
# #     def documento(self):
# #         f = open("C:/load/txt/pruebaDjangofile.txt" ,"w+")
# #         f.write("ENC,DS,DIAN 2.1: Documento soporte en adquisiciones efectuadas a no obligados a facturar.,DME1503," + time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime()) +"-05:00," + "05,COP,1,2,10,UBL 2.1\n")
# #         f.write("CUD,123456789ASD0987654321\n")
# #         f.write("EMI,1,,11001,Bogotá D.C.,110111,Bogotá,11,CRA 72 80-94 OF 902 CTRO EMP. TITAN PLAZA,CO,Colombia,,Black & Decker de Colombia S.A.S,935462718,1,31 \n")
# #         f.close()


