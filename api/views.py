from django.shortcuts import render,redirect
from .forms import EmployerSignUpForm,InstitutionSignUpForm,LoginForm
from .models import *
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

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
        return redirect('login_view')

class InstitutionSignUpView(CreateView):
    model = User
    form_class = InstitutionSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs ['user_type'] = 'institution'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('login_view')

def login_view(request):
  form = LoginForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,password=password)
      if user is not None and user.is_employer:
        login(request, user)
        return redirect('home')
      elif user is not None and user.is_institution:
        login(request, user)
        return redirect('home')
  return render (request, 'login.html',{'form':form})

def home(request):
  return render(request,'home.html' )

def create_learner(request):
  current_user = request.user
  title = "Create Learner"
  if request.method == 'POST':
      learner_form = ProfileForm(request.POST, request.FILES)
      if learner_form.is_valid():
          learner = learner_form.save(commit=False)
          learner.user = current_user
          learner.save()
      return HttpResponseRedirect('/')

  else:
      learner_form = ProfileForm()
  return render(request, 'create_learner.html', {"learner_form": learner_form, "title": title})