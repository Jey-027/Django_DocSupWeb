from .forms import documentoForm
from django.shortcuts import redirect, render
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
    paginate_by = 20

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
        ,"payment_date"
        #,"user_process"
    ]

    initial = {
        "Date_process": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), 
        "status": 1 }

    success_url = "/facturas/list"

    # if success_url == "/facturas/list":
        # ocreatefile = CreateFile()
        # ocreatefile.genera_documento()
    

# class CreateFile():
   
    
#     def genera_documento(self):
#         f = open("C:/load/txt/pruebaDjangofile.txt" ,"w+")
#         f.write("ENC,DS,DIAN 2.1: Documento soporte en adquisiciones efectuadas a no obligados a facturar.,DME1503," + time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime()) +"-05:00," + "05,COP,1," + "FECHA DE PAGO" + ",2,10,UBL 2.1\n")
#         f.write("CUD,123456789ASD0987654321\n")
#         f.write("EMI,1,,11001,Bogotá D.C.,110111,Bogotá,11,CRA 72 80-94 OF 902 CTRO EMP. TITAN PLAZA,CO,Colombia,,Black & Decker de Colombia S.A.S,935462718,1,31 \n")
#         f.write("TAC,O-13\n")
#         f.write("GTE,01,IVA\n" + "ACA DEBE IR EL CAMPO DE LA LISTA -- "   + "\n")
#         f.close()



# def updateDocumento(request, id):
#     doc = documento.objects.get(id = id)

#     if request.method == "GET":
#         form = documentoForm(instance=doc)
#     else:
#         form = documentoForm(request.POST, instance=doc)
#         if form.is_valid():
#             doc.status = 1
#             form.save()
#             ocreatefile = CreateFile()
#             ocreatefile.genera_documento()
#         return redirect("Detalle_facturacion")
#     return render(request, "DocSupApp/generacion_documento.html", {"form": form})



def updateDocumento(request, id):
    doc = documento.objects.get(id = id)

    if request.method == "GET":
        form = documentoForm(instance=doc)
    else:
        form = documentoForm(request.POST, instance=doc)
        if form.is_valid():
            doc.status = 1
            form.save()
            
        f = open("C:/load/txt/pruebaDjangofile501.txt" ,"w+")
        f.write("ENC,DS,DIAN 2.1: Documento soporte en adquisiciones efectuadas a no obligados a facturar.,DME1503," + time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime()) +"-05:00," + "05,COP,1," + "%s"%doc.payment_date + ",2,10,UBL 2.1\n")
        f.write("CUD,123456789ASD0987654321\n")
        f.write("EMI,1,,11001,Bogotá D.C.,110111,Bogotá,11,CRA 72 80-94 OF 902 CTRO EMP. TITAN PLAZA,CO,Colombia,,Black & Decker de Colombia S.A.S,935462718,1,31 \n")
        f.write("TAC,O-13\n")
        f.write("GTE,01,IVA\n")   
        f.write("ADQ,1,,,,,,,,,," + "%s"%doc.Nit + ",, " + "%s"%doc.type_of_tax_number + "," + "%s"%doc.suplier_tax_code + "\n")
        f.write("TCR,O-13;O-15\n")  ## VALIDAR SI ES 13 0 15
        f.write("GTA,01,IVA\n") 
        f.write("TOT," + "%s"%doc.net_amount + ",COP," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.net_amount  + ",COP,0.00,COP,0.00,COP,,,,\n")
        f.write("TIM,false,0.00,COP\n")
        f.write("IMP,01," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.tax_amount + ",COP,19.00\n")	
        f.write("TIM,true,4000.00,COP\n") ## VALIDAR
        f.write("IMP,06,100000.00,COP,4000.00,COP,4.00\n") ## VALIDAR
        f.write("DSC,false,0,0.00,COP,01,," + "%s"%doc.net_amount + ",COP,1 \n")
        f.write("DRF,32912731242012,2019-11-26,2022-11-26,DME,1,5000000\n") ## VALIDAR
        f.write("NOT,1_Responsable de impuesto sobre las ventas - IVA - Agentes Retenedores de IVA.\n")
        f.write("MEP,1,2,2020-06-26\n") ## CREAR UNA TABLA DE LOS CODIGOS DE METODO DE PAGO Y TRAER LOS DATOS DE AHI Y VALIDAR SI LA FECHA DE CREDITO DEBE INSERTAR EL USUARIO
        f.write("IDP,IDP1\n")
        f.write("CTS,CE01\n")
        f.write("ITE,1,1,94," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.net_amount  + ",COP,," + "%s"%doc.item_description + ",1,VALIDARCODIGOVENDEDOR,1,94,," + "%s"%doc.net_amount + ",COP,,,,\n")
        f.write("FCB," + "%s"%doc.date_Invoice + ",1,Por operación\n")
        f.write("MYM,Carvajal,CTS\n") # PREGUNTAR CARVAJAL
        f.write("IAE,12345,999,,Estándar de adopción del contribuyente\n") # PREGUNTAR CARVAJAL
        f.write("TII," + "%s"%doc.tax_amount + ",COP,false\n")
        f.write("IIM,01," + "%s"%doc.tax_amount + ",COP," + "%s"%doc.net_amount + ",COP,19.00\n") # validar IVA
        f.write("DIT," + "%s"%doc.tax_amount + "\n")
        f.write("NTI,\n")
        f.write("NTI,\n")
        f.write("NTI,\n")
        f.write("ORP," + "%s"%doc.id + "," + "%s"%doc.payment_date + "\n")
        f.close()

        return redirect("Detalle_facturacion")
    return render(request, "DocSupApp/generacion_documento.html", {"form": form})





