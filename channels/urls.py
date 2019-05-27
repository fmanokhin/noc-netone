from django.conf.urls import url
from . import views

urlpatterns = [
#Каналы L2VPN:
    url(r'^channels/l2vpn/$', views.l2vpn_list, name='l2vpn_list'),
    url(r'^channels/l2vpn/(?P<pk>\d+)/$', views.l2vpn_detail, name='l2vpn_detail'),
    url(r'^channels/l2vpn/new/$', views.l2vpn_new, name='l2vpn_new'),
    url(r'^channels/l2vpn/(?P<pk>\d+)/edit/$', views.l2vpn_edit, name='l2vpn_edit'),
    url(r'^channels/l2vpn/(?P<pk>\d+)/remove/$', views.l2vpn_remove, name='l2vpn_remove'),
]
