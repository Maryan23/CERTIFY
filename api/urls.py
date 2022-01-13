from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns=[
    path('' ,views.index ,name='index'),
    path('signup/',views.SignUp,name = 'Signup'),
    path('accounts/signup/employer/',views.EmployerSignUpView.as_view(), name = 'employer_signup'),
    path('accounts/signup/institution/',views.InstitutionSignUpView.as_view(), name = 'institution_signup')
]