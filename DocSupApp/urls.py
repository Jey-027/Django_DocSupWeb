from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Home" ),
    path('account/', include("django.contrib.auth.urls"), name="login"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('vendor/list', views.vendorList.as_view(), name="vendorList"),
    path('vendor/create', views.VendorCreate.as_view(), name="Vendor_create"),
    path('vendor/update/<pk>', views.VendorUpdate.as_view(), name="Vendor_Update"),
    path('facturas/list', views.DetFactList.as_view(), name="Detalle_facturacion"),
    path('facturas/generar/<pk>', views.DetFactUpdate.as_view(), name="Genera_file"),
]

