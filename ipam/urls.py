from django.conf.urls import url
from . import views

urlpatterns = [

#IPv4
    url(r'^ipam/ipv4/$', views.ipv4_list, name='ipv4_list'),
    url(r'^ipam/ipv4/(?P<pk>\d+)/$', views.ipv4_detail, name='ipv4_detail'),
    url(r'^ipam/ipv4/new/$', views.ipv4_new, name='ipv4_new'),
    url(r'^ipam/ipv4/(?P<pk>\d+)/edit/$', views.ipv4_edit, name='ipv4_edit'),
    url(r'^ipam/ipv4/(?P<pk>\d+)/remove/$', views.ipv4_remove, name='ipv4_remove'),
    url(r'^ipam/ipv4/(?P<pk>\d+)/sepor/$', views.ipv4_sepor, name='ipv4_sepor'),
]
