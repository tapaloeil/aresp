from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.animal_list, name='animal_list'),
    url(r'^animal/(?P<pk>\d+)/$', views.animal_detail, name='animal_detail'),
]