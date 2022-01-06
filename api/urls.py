from django.urls import path
from . import views

urlpatterns=[
    path('api/employers/',views.EmployerList.as_view())

]