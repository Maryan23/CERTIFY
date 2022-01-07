from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^institutions/api/$', views.institutionAPI),
  url(r'^institutions/api/([0-9]+)$', views.institutionAPI),
  url(r'^learners/api/$', views.LearnerAPI),
  url(r'^learners/api/([0-9]+)$', views.LearnerAPI),
]

