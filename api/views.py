from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

#Create your views
def index(request):
  return render(request,'index.html' )



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