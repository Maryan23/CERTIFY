from django.conf.urls import url
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('register/', include('rest_framework.urls', namespace='rest_framework')),
  path('auth/', ObtainAuthToken.as_view()),
  url(r'^institutions/api/$', views.institutionAPI),
  url(r'^institutions/api/([0-9]+)$', views.institutionAPI),
  url(r'^learners/api/$', views.LearnerAPI),
  url(r'^learners/api/([0-9]+)$', views.LearnerAPI),
]

