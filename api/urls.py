from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('' ,views.index ,name='index'),
    path('learner/<learner_id>',views.learner,name ='learner'),
    path('signup/',views.SignUp,name = 'Signup'),
    path('accounts/signup/employer/',views.EmployerSignUpView.as_view(), name = 'employer_signup'),
    path('accounts/signup/institution/',views.InstitutionSignUpView.as_view(), name = 'institution_signup'),
    path('login/',views.login_view, name = 'login_view'),
    path('logout/',views.logout, name = 'logout'),
    path('institution/' ,views.institution ,name='institution'),
    path('create_learner/',views.create_learner,name = 'create_learner'),
    path('employer/', views.employer, name='employer'),
    path('search',views.search, name='search'),
    path('institution/' ,views.institution ,name='institution'),
    path('learner/<int:learner_id>/',views.learner,name='learner'),
    path('update_learner/<learner_id>',views.update_learner,name='update_learner'),
    path('delete_learner/<learner_id>',views.delete_learner,name='delete_learner'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
