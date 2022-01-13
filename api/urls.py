from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns=[
    path('' ,views.index ,name='index'),
    path('employer/<int:id>/', views.employer, name='employer'),
    path('search',views.search, name='search'),
]