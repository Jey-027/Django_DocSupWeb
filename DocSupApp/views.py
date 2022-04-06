from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from .models import documento, proveedor, documento
from django.urls import reverse_lazy
import time
from .file import CreateFile
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
    context_object_name = "proveedor_list"

class VendorCreate(CreateView):
    model = proveedor
    template_name = "DocSupApp/proveedor_create.html"
    fields = "__all__"
    success_url = "/vendor/list"

class VendorUpdate(UpdateView):
    model = proveedor
    template_name = "DocSupApp/proveedor_update.html"
    fields = "__all__"
    success_url = "/vendor/list"

# aqui van las view sobre la generacion del documento

class DetFactList(ListView):
    model = documento
    context_object_name = "lista_de_Documentos"

class DetFactUpdate(UpdateView):
    model = documento
    template_name = "DocSupApp/Genera_file.html"
    fields = [
        "Date_process"
        ,"id"
        ,"id_supplier_vendor"
        ,"name_supplier_vendor"
        ,"id_supplier_invoice"
        ,"zSupplierID"
        ,"net_amount"
        ,"status" 
        #,"user_process"
    ]
    initial = {
        "Date_process": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), 
        "status": 1 }

    success_url = "/facturas/list"

    

    def validate():
        newList = []
        query = documento.objects.all()
        for row in query:
            newList.append(row[0])
            newList.append(row[2]) 


    if success_url == "/facturas/list":
        ocreatefile = CreateFile()
        ocreatefile.genera_documento()
    





