from django.conf.urls import url
from . import views
urlpatterns = [
      url(r'^api/projects/$', views.LearnerstList.as_view()),
]
