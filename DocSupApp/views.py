from django.http import HttpResponse
from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from .models import documento, proveedor, documento
from django.urls import reverse_lazy
from .forms import documentoForm
import time
# Create your views here.


# def login_view(request):
#     context = {
#         "login_view": "active"
#     }
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password = password)

#         if user is not None:
#             login(request, user)
#             return redirect("Home")

#         else:
#             return HttpResponse("Invalid credentials")
#     return render(request, "registration/login.html", context)

def logout_view(request):
  logout(request)
  return redirect("Home")


@login_required
def home(request):
    context = {"name": "<Put your name here>"}
    return render(request, "DocSupApp/home.html", context)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class vendorList(LoginRequiredMixin,ListView):
    model = proveedor
    context_object_name = "proveedor_list"
    paginate_by = 20

class VendorCreate(LoginRequiredMixin,CreateView):
    model = proveedor
    template_name = "DocSupApp/proveedor_create.html"
    fields = "__all__"
    success_url = "/vendor/list"

class VendorUpdate(LoginRequiredMixin,UpdateView):
    model = proveedor
    template_name = "DocSupApp/proveedor_update.html"
    fields = "__all__"
    success_url = "/vendor/list"

# aqui van las view sobre la generacion del documento

class DetFactList(LoginRequiredMixin,ListView):
    model = documento
    context_object_name = "lista_de_Documentos"



class DetFactUpdate(LoginRequiredMixin,UpdateView):
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
        ,"payment_date"
        #,"user_process"
    ]

    initial = {
        "Date_process": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), 
        "status": 1 }

    success_url = "/facturas/list"

def updateDocumento(request, id):
    doc = documento.objects.get(id = id)

    if request.method == "GET":
        form = documentoForm(instance=doc)
    else:
        form = documentoForm(request.POST, instance=doc)
        if form.is_valid():
            doc.status = 1
            form.save()
            
        f = open("C:/load/txt/pruebaDjangofile502.txt" ,"w+")
        f.write("ENC,DS,DIAN 2.1: Documento soporte en adquisiciones efectuadas a no obligados a facturar.,DME1503," + time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime()) +"-05:00," + "05,COP,1," + "%s"%doc.payment_date + ",2,10,UBL 2.1\n")
        f.write("CUD,\n")
        f.write("EMI,2,," + "%s"%doc.city_id + "," +"%s"%doc.city_name + "," + "%s"%doc.city_id + "%s"%doc.est_fed_prov + "," + "%s"%doc.city_name + "," + "%s"%doc.est_fed_prov + "," + "%s"%doc.address + "," + "%s"%doc.country + ",Colombia,," + "%s"%doc.name_supplier_vendor + "," + "%s"%doc.Nit + ",DV," + "%s"%doc.type_of_tax_number + "\n") # informacion del proveedor
        f.write("TAC,R-99-PN\n")
        f.write("GTE,ZZ,IVA\n")   
        f.write("ADQ,1,,,,,,,,,,860070698,,1,31,Black & Decker de Colombia S.A.S\n") 
        f.write("TCR,O-13\n")
        f.write("GTA,01,IVA\n") 
        f.write("TOT," + "%s"%doc.net_amount + ",COP," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.net_amount  + ",COP,0.00,COP,0.00,COP,,,,\n")
        f.write("TIM,true,0.00,COP\n")
        f.write("IMP,01," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.tax_amount + ",COP,19.00\n")	
        f.write("DRF,19890900900,2019-01-19,2030-01-19,DSA,5000001,8000000\n")
        f.write("NOT,1_Responsable de impuesto sobre las ventas - IVA - Agentes Retenedores de IVA.\n")
        f.write("MEP,1,2," +  "deberia ir el payment date" + "2020-06-26\n") ## CREAR UNA TABLA DE LOS CODIGOS DE METODO DE PAGO Y TRAER LOS DATOS DE AHI Y VALIDAR SI LA FECHA DE CREDITO DEBE INSERTAR EL USUARIO
        f.write("ITE,1,1,94," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.net_amount  + ",COP,," + "%s"%doc.item_description + ",1,VALIDARCODIGOVENDEDOR,1,94,," + "%s"%doc.net_amount + ",COP,,,,\n") # valdia codigo
        f.write("FCB," + "%s"%doc.date_Invoice + ",1,Por operación\n")
        f.write("TII," + "%s"%doc.tax_amount + ",COP,false\n")
        f.write("IIM,01," + "%s"%doc.tax_amount + ",COP," + "%s"%doc.net_amount + ",COP,19.00\n")
        f.close()

        return redirect("Detalle_facturacion")
    return render(request, "DocSupApp/generacion_documento.html", {"form": form})





