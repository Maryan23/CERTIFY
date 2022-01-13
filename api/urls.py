from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns=[
    path('' ,views.index ,name='index'),
    path('institution' ,views.institution ,name='institution'),
    path('learner/<int:learner_id>/',views.learner,name='learner'),
    path('update_learner/<learner_id>',views.update_learner,name='update_learner'),
    path('delete_learner/<learner_id>',views.delete_learner,name='delete_learner'),
]