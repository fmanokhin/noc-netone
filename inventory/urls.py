from django.conf.urls import url
from . import views

urlpatterns = [
# Точки присутствия:
    url(r'^internet/pops/$', views.pop_list, name='pop_list'),
    url(r'^internet/pop/(?P<pk>\d+)/$', views.pop_detail, name='pop_detail'),
    url(r'^internet/pop/new/$', views.pop_new, name='pop_new'),
    url(r'^internet/pop/(?P<pk>\d+)/edit/$', views.pop_edit, name='pop_edit'),
    url(r'^internet/pop/(?P<pk>\d+)/remove/$', views.pop_remove, name='pop_remove'),
]
