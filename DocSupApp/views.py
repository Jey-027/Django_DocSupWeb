from .models import documento, proveedor, documento, properties
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.http.response import  HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import documentoForm
from django.conf import settings
from django.db.models import Q
from datetime import datetime
from openpyxl import Workbook
import time
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect("Home")


class homeView(LoginRequiredMixin, TemplateView):
    template_name = "DocSupApp/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documento"] = documento.objects.all()
        context["documentoNull"] = documento.objects.filter(~Q(status=1))
        context["documento1"] = documento.objects.filter(status=1)
        context["proveedor"] = proveedor.objects.all()
        return context


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class vendorList(LoginRequiredMixin,ListView):
    model = proveedor
    context_object_name = "proveedor_list"
    #paginate_by = 20

    def buscar(request):
        queryset = request.GET.get("Search")
        # vendor = proveedor.objects.filter(estado = True)
        print(queryset)
        if queryset:
            vendor = proveedor.objects.filter(
                Q(name__icontains = queryset) |
                Q(id_supplier__icontains = queryset)
            ).distinct()
        return render(request, 'proveedor_list.html', {'vendor': vendor})

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


def updateDocumento(request, id):
    doc = documento.objects.get(id = id)

    numRes = properties.objects.first()
    name_file = numRes.path_file + numRes.name_file + str(numRes.Num_resolution) + ".txt"

    if request.method == "GET":
        form = documentoForm(instance=doc)
    else:
        form = documentoForm(request.POST, instance=doc)
        if form.is_valid():
            doc.num_documento = numRes.name_file + str(numRes.Num_resolution)
            doc.Date_process = datetime.now()
            doc.status = 1
            doc.user_process = str(request.user)
            form.save()
            messages.add_message(request=request, level=messages.SUCCESS, message="Documento generado correctamente!")
            
            f = open("%s"%name_file ,"w+")
            f.write("ENC,INVOIC,DIAN 2.1: documento soporte en adquisiciones efectuadas a no obligados a facturar.," + "%s"%numRes.prefijo_res + "%s"%numRes.Num_resolution  + "," + time.strftime('%Y-%m-%d,%H:%M:%S', time.localtime()) +"-05:00," + "05,COP,1," + "%s"%doc.payment_date + ",2,10,UBL 2.1\n")
            f.write("CUD,\n")
            f.write("EMI," + "%s"%doc.tipo_persona + ",," + "%s"%doc.city_id + "," +"%s"%doc.city_name + "," + "%s"%doc.city_id + "%s"%doc.est_fed_prov + "," + "%s"%doc.city_name + "," + "%s"%doc.est_fed_prov + "," + "%s"%doc.address + "," + "%s"%doc.country + ",Colombia,," + "%s"%doc.name_supplier_vendor + "," + "%s"%doc.Nit + ",," + "%s"%doc.type_of_tax_number + "\n") # informacion del proveedor
            f.write("TAC,R-99-PN\n")
            f.write("GTE,ZZ,IVA\n")   
            f.write("ADQ,1,,,,,,,,,,860070698,1,31,Black & Decker de Colombia S.A.S\n") 
            f.write("TCR,O-13\n")
            f.write("GTA,01,IVA\n") 
            f.write("TOT," + "%s"%doc.net_amount + ",COP," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.net_amount  + ",COP,0.00,COP,0.00,COP,,,,\n")
            f.write("TIM,true,0.00,COP\n")
            f.write("IMP,01," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.tax_amount + ",COP,19.00\n")	
            f.write("DRF,"+ "%s"%numRes.autorization + "," + "%s"%numRes.start_date_res + "," + "%s"%numRes.end_date_res + "," + "%s"%numRes.prefijo_res + "," + "%s"%numRes.initial_range_res + "," + "%s"%numRes.end_range_res + "\n")
            f.write("NOT,1_Responsable de impuesto sobre las ventas - IVA - Agentes Retenedores de IVA.\n")
            f.write("MEP,1,2," +  "%s"%doc.payment_date + "\n") ## VALIDAR SI LA FECHA DE CREDITO DEBE INSERTAR EL USUARIO
            f.write("ITE,1,1,94," + "%s"%doc.net_amount  + ",COP," + "%s"%doc.net_amount  + ",COP,," + "%s"%doc.item_description + ",1," + "%s"%doc.zSupplierID  + ",1,94,1," + "%s"%doc.net_amount + ",COP,,,,\n") # validar codigo vendedor
            f.write("FCB," + "%s"%doc.date_Invoice + ",1,Por operación\n")
            f.write("TII," + "%s"%doc.tax_amount + ",COP,false\n")
            f.write("IIM,01," + "%s"%doc.tax_amount + ",COP," + "%s"%doc.net_amount + ",COP,0.00\n")
            f.close()

            if numRes.Num_resolution >= 5000030:
                subject = "advertencia numero consecutivo doc soporte"
                message = "este correo es para notificar que su numero de resolucion es " + str(numRes.Num_resolution) + "para que vaya solicitando su nuevo rango"
                email_from = settings.EMAIL_HOST_USER
                recipient_list=["jdrodriguezg25@hotmail.com"]
                send_mail(subject, message, email_from, recipient_list)


            numRes.Num_resolution += 1
            numRes.save()

        return redirect("Detalle_facturacion")
    return render(request, "DocSupApp/generacion_documento.html", {"form": form})


class reporteExcelVendor(TemplateView):
    def get(self, request, *args, **kwargs):
        vendor = proveedor.objects.all()
        wb = Workbook()
        ws = wb.active
        ws["A1"]= "REPORTE DE PROVEEDORES"

        ws.merge_cells("A1:N1")
        ws["A3"]= "Id Supplier"
        ws["B3"]= "Name"
        ws["C3"]= "Tax code"
        ws["D3"]= "city id"
        ws["E3"]= "City Name"
        ws["F3"]= "Email"
        ws["G3"]= "Nit"
        ws["H3"]= "Tax Description"
        ws["I3"]= "Type of tax number"
        ws["J3"]= "Address"
        ws["K3"]= "Country"
        ws["L3"]= "Estado federal"
        ws["M3"]= "name estado federal"
        ws["N3"]= "Currency type"

        cont = 4

        for vendor in vendor:
            ws.cell(row= cont, column= 1).value = vendor.id_supplier
            ws.cell(row= cont, column= 2).value = vendor.name
            ws.cell(row= cont, column= 3).value = vendor.supplier_tax_code
            ws.cell(row= cont, column= 4).value = vendor.city_id
            ws.cell(row= cont, column= 5).value = vendor.city_name
            ws.cell(row= cont, column= 6).value = vendor.email
            ws.cell(row= cont, column= 7).value = vendor.nit
            ws.cell(row= cont, column= 8).value = vendor.supplier_tax_description
            ws.cell(row= cont, column= 9).value = vendor.Type_of_tax_number
            ws.cell(row= cont, column= 10).value = vendor.address
            ws.cell(row= cont, column= 11).value = vendor.country
            ws.cell(row= cont, column= 12).value = vendor.est_fed_prov
            ws.cell(row= cont, column= 13).value = vendor.name_est_fed_prov
            ws.cell(row= cont, column= 14).value = vendor.currency_type
            cont += 1

        file_name = "ReporteProveedores.xlsx"
        response = HttpResponse(content_type = "application/ms-excel")
        content = "attachment; filename = {0}".format(file_name)
        response["Content-Disposition"] = content
        wb.save(response)
        return response

class reporteListaDocumentos(TemplateView):
    def get(self,request, *args, **kwargs):
        document = documento.objects.all()
        wb = Workbook()
        ws = wb.active
        ws["A1"]= "REPORTE DE DOCUMENTOS "

        ws.merge_cells("A1:N1")
        ws["A3"]= "Id supplier vendor"
        ws["B3"]= "Name vendor"
        ws["C3"]= "Tax code"
        ws["D3"]= "City Name"
        ws["E3"]= "Nit"
        ws["F3"]= "Type tax number"
        ws["G3"]= "Currency type"
        ws["H3"]= "Supplier id"
        ws["I3"]= "Name supplier customer"
        ws["J3"]= "COFP"
        ws["K3"]= "Date invoice"
        ws["L3"]= "Item description"
        ws["M3"]= "ZsupplierID"
        ws["N3"]= "zSupplierName"
        ws["O3"]= "Net Amount"
        ws["P3"]= "Tax Amount"
        ws["Q3"]= "Gross Amount"
        ws["R3"]= "Percent RTE"
        ws["S3"]= "Percent IVA"
        ws["T3"]= "Percent ICA"
        ws["U3"]= "Amount IVA"
        ws["V3"]= "Amount RTE"
        ws["W3"]= "Amount ICA"
        ws["X3"]= "Value RTE"
        ws["Y3"]= "Total Retenciones"
        ws["Z3"]= "Person Type"
        ws["AA3"]= "Status"
        ws["AB3"]= "Date Process"
        ws["AC3"]= "User Process"
        ws["AD3"]= "Payment date"
        ws["AE3"]= "Document number"

        cont = 4

        for document in document:
            ws.cell(row= cont, column=1).value = document.id_supplier_vendor
            ws.cell(row= cont, column=2).value = document.name_supplier_vendor
            ws.cell(row= cont, column=3).value = document.suplier_tax_code
            ws.cell(row= cont, column=4).value = document.city_name
            ws.cell(row= cont, column=5).value = document.Nit
            ws.cell(row= cont, column=6).value = document.type_of_tax_number
            ws.cell(row= cont, column=7).value = document.currency_type
            ws.cell(row= cont, column=8).value = document.supplier_id_Customer
            ws.cell(row= cont, column=9).value = document.name_supplier_customer
            ws.cell(row= cont, column=10).value = document.id_supplier_invoice
            ws.cell(row= cont, column=11).value = document.date_Invoice
            ws.cell(row= cont, column=12).value = document.item_description
            ws.cell(row= cont, column=13).value = document.zSupplierID
            ws.cell(row= cont, column=14).value = document.zSupplierName
            ws.cell(row= cont, column=15).value = document.net_amount
            ws.cell(row= cont, column=16).value = document.tax_amount
            ws.cell(row= cont, column=17).value = document.gross_amount
            ws.cell(row= cont, column=18).value = document.percent_RTE
            ws.cell(row= cont, column=19).value = document.percent_IVA
            ws.cell(row= cont, column=20).value = document.percent_ICA
            ws.cell(row= cont, column=21).value = document.amount_RTE
            ws.cell(row= cont, column=22).value = document.amount_IVA
            ws.cell(row= cont, column=23).value = document.amount_ICA
            ws.cell(row= cont, column=24).value = document.Value_RTE
            ws.cell(row= cont, column=25).value = document.total_retenciones
            ws.cell(row= cont, column=26).value = document.tipo_persona
            ws.cell(row= cont, column=27).value = document.status
            ws.cell(row= cont, column=28).value = document.Date_process
            ws.cell(row= cont, column=29).value = document.user_process
            ws.cell(row= cont, column=30).value = document.payment_date
            ws.cell(row= cont, column=31).value = document.num_documento
            cont +=1

        file_name = "ReporteDocumentos.xlsx"
        response = HttpResponse(content_type = "application/ms-excel")
        content = "attachment; filename = {0}".format(file_name)
        response["Content-Disposition"] = content
        wb.save(response)
        return response



  


