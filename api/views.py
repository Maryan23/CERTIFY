from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render,redirect
from .forms import EmployerSignUpForm,InstitutionSignUpForm,LoginForm,LearnerForm,CreateLearnerForm, UpdateLearnerForm
from api.models import *
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView

#Create your views
def index(request):
  return render(request,'index.html' )

@login_required(login_url='/accounts/login')
def learner(request, learner_id):
    try:
        learner = Learner.filter_by_id(id=learner_id)
    except Learner.DoesNotExist:
        raise Http404()
    return render(request, "learner.html",{"learner":learner} )

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
        return redirect('employer')
      elif user is not None and user.is_institution:
        login(request, user)
        return redirect('institution')
  return render (request, 'login.html',{'form':form})

def logout(request):
  auth.logout(request)
  return redirect ('/')

def institution(request):
  return render(request,'institution.html' )

def create_learner(request):
  current_user = request.user
  title = "Create Learner"
  if request.method == 'POST':
      learner_form = LearnerForm(request.POST, request.FILES)
      if learner_form.is_valid():
          learner = learner_form.save(commit=False)
          learner.user = current_user
          learner.save()
      return redirect('institution')

  else:
      learner_form = LearnerForm()
  return render(request, 'create_learner.html', {"learner_form": learner_form, "title": title})


@login_required
def employer(request, id):
    employer = Employer.objects.get(id=id)
    certificates = Certificate.objects.filter(id = id)
    current_user = request.user
    return render(request, 'employer.html', {'certificates': certificates, 'employer': employer, 'current_user':current_user})


@login_required
def search(request):
    if 'first_name' in request.GET and request.GET['first_name']:
        search_term = request.GET.get('first_name')
        search_learners = Learner.search_by_learner_name(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {'message': message, 'learners': search_learners})

    else:
        message = "You have not search for any learner."
        return render(request, 'search.html', {'message': message})

def institution(request):
  # institution = Institution.filter_by_reg_no(reg_no)
  return render(request,'institution.html',{"institution":institution})

def learner(request, learner_id):
    current_user = request.user
    learner = Learner.objects.get(id=learner_id)
    learner = Learner.objects.filter(learner=learner)
    return render(request, 'intitution.html', {'current_user':current_user, 'institution':institution,'learner':learner})

def create_learner(request):
    if request.method == 'POST':
        create_learner_form = CreateLearnerForm(request.POST, request.FILES)
        if create_learner_form.is_valid():
            learner = create_learner_form.save(commit=False)
            learner.admin = request.user.profile
            learner.save()
            return redirect('home')
    else:
        create_learner_form = CreateLearnerForm()
    return render(request, 'newlearner.html', {'create_learner_form': create_learner_form})


def update_learner(request, learner_id):
    learner = Learner.objects.get(pk=learner_id)
    if request.method == 'POST':
        update_learner_form = UpdateLearnerForm(request.POST,request.FILES, instance=learner)
        if update_learner_form.is_valid():
            update_learner_form.save()
            messages.success(request, f'Learner updated!')
            return redirect('home')
    else:
        update_learner_form = UpdateLearnerForm(instance=learner)

    return render(request, 'update_learner.html', {"update_learner_form":update_learner_form})

def delete_learner(request,learner_id):
    current_user = request.user
    learner = Learner.objects.get(pk=learner_id)
    if learner:
        learner.delete_learner()
    return redirect('home')
