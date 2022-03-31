
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import proveedor
from django.urls import reverse_lazy
# Create your views here.


@login_required
def home(request):
    context = {"name": request.user.username}
    return render(request, "DocSupApp/home.html", context)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'




class vendorList(LoginRequiredMixin,ListView):
    model = proveedor


