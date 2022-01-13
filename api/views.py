from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Learner
from django.contrib.auth.models import User

#Create your views
def index(request):
  return render(request,'index.html' )

@login_required(login_url='/accounts/login')
def learner(request, learner_id):
    try:
        learner = Learner.filter_by_id(id=learner_id)
    except learner.DoesNotExist:
        raise Http404()
    return render(request, "learner.html",{"learner":learner} )

