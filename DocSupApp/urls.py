from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Home" ),
    path('account/', include("django.contrib.auth.urls"), name="login"),
    path('vendor/list', views.vendorList.as_view(), name="vendorList"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]

