from django.shortcuts import render

#Create your views
def index(request):
  return render(request,'index.html' )