from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView.as_view(), name="Home" ),
    path('accounts/', include("django.contrib.auth.urls"), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('vendor/list', views.vendorList.as_view(), name="vendorList"),
    path('search/', views.search, name="Search"),
    path('vendor/create', views.VendorCreate.as_view(), name="Vendor_create"),
    path('vendor/update/<pk>', views.VendorUpdate.as_view(), name="Vendor_Update"),
    path('facturas/list', views.DetFactList.as_view(), name="Detalle_facturacion"),
    path('generaDocumento/<id>', views.updateDocumento, name="Documento_generado"),
    path('no_envia_documento/<id>', views.noSendFile, name="Documento_no_enviado"),
    path('documentos/list', views.detalle_documentos.as_view(), name="Doc_generadas"),
    path('genera_nota_credito/<id>', views.genera_notaCredito, name="Notas_credito"),
    path('reporte_excel_vendor/', views.reporteExcelVendor.as_view(), name="Reporte_Excel_vendor"),
    path('reporte_Documentos/', views.reporteListaDocumentos.as_view(), name="Reporte_Documentos"),
]


