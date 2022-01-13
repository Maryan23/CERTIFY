from django.shortcuts import render,redirect
from .forms import EmployerSignUpForm,InstitutionSignUpForm
from .models import *
from django.contrib.auth import login
from django.views.generic import CreateView

#Create your views
def index(request):
  return render(request,'index.html' )

def SignUp(request):
    return render(request,'register.html')

class EmployerSignUpView(CreateView):
    model = User
    form_class = EmployerSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('index')

class InstitutionSignUpView(CreateView):
    model = User
    form_class = InstitutionSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'institution'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('index')