from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import ObtainAuthToken



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('api/employers/',views.EmployerList),
    path('register/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/',ObtainAuthToken.as_view())


]