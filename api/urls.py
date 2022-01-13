from django.urls import path
from . import views


urlpatterns=[
    path('' ,views.index ,name='index'),
    path('signup/',views.SignUp,name = 'Signup'),
    path('accounts/signup/employer/',views.EmployerSignUpView.as_view(), name = 'employer_signup'),
    path('accounts/signup/institution/',views.InstitutionSignUpView.as_view(), name = 'institution_signup'),
    path('login/',views.login_view, name = 'login_view'),
    path('logout/',views.logout, name = 'logout'),
    path('institution/' ,views.institution ,name='institution'),
    path('create_learner/',views.create_learner,name = 'create_learner'),
    path('employer/<int:id>/', views.employer, name='employer'),
    path('search',views.search, name='search'),
]