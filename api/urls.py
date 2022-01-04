from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^api/institutions/$', views.InstitutionList.as_view()),
  url(r'^api/learners/$', views.LearnerList.as_view()),
]

