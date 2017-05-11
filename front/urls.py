from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.animal_list, name='animal_list'),
    url(r'^drafts/$', views.animal_draft_list, name='animal_draft_list'),
    url(r'^animal/(?P<pk>\d+)/$', views.animal_detail, name='animal_detail'),
    url(r'^animal/new/$', views.animal_new, name='animal_new'),
    url(r'^animal/(?P<pk>\d+)/edit/$', views.animal_edit, name='animal_edit'),
    url(r'^animal/(?P<pk>\d+)/publier/$', views.animal_publier, name='animal_publier'),
    url(r'^animal/(?P<pk>\d+)/delete/$', views.animal_delete, name='animal_delete'),
]