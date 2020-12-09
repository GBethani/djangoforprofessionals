from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserChangeForm,CustomUserCreationForm
# Create your views here.

class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'