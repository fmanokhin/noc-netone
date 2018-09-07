from django.conf.urls import url
from . import views

urlpatterns = [
# Точки присутствия:
    url(r'^internet/pops/$', views.pop_list, name='pop_list'),
    url(r'^internet/pop/(?P<pk>\d+)/$', views.pop_detail, name='pop_detail'),
    url(r'^internet/pop/new/$', views.pop_new, name='pop_new'),
    url(r'^internet/pop/(?P<pk>\d+)/edit/$', views.pop_edit, name='pop_edit'),
    url(r'^internet/pop/(?P<pk>\d+)/remove/$', views.pop_remove, name='pop_remove'),

# Опорные узлы:
    url(r'^internet/cores/$', views.core_list, name='core_list'),
    url(r'^internet/core/(?P<pk>\d+)/$', views.core_detail, name='core_detail'),
    url(r'^internet/core/new/$', views.core_new, name='core_new'),
    url(r'^internet/core/(?P<pk>\d+)/edit/$', views.core_edit, name='core_edit'),
    url(r'^internet/core/(?P<pk>\d+)/remove/$', views.core_remove, name='core_remove'),

# Связки:
# На Корах (оборудование)
    url(r'^internet/core/(?P<pk>\d+)/edit/devices/$', views.core_devices, name='core_devices'),
    url(r'^internet/core/(?P<corepk>\d+)/devices/remove/(?P<devicepk>\d+)/$', views.core_device_remove, name='core_device_remove'),
    url(r'^internet/core/(?P<corepk>\d+)/devices/add/(?P<devicepk>\d+)/$', views.core_device_add, name='core_device_add'),
# На Корах (даунстримы)
    url(r'^internet/core/(?P<pk>\d+)/edit/downstreams/$', views.core_downstreams, name='core_downstreams'),
    url(r'^internet/core/(?P<corepk>\d+)/downstreams/remove/(?P<poppk>\d+)/$', views.core_downstreams_remove, name='core_downstreams_remove'),
    url(r'^internet/core/(?P<corepk>\d+)/downstreams/add/(?P<poppk>\d+)/$', views.core_downstreams_add, name='core_downstreams_add'),
# На Точках присутствия (оборудование)
    url(r'^internet/pop/(?P<pk>\d+)/edit/devices/$', views.pop_devices, name='pop_devices'),
    url(r'^internet/pop/(?P<poppk>\d+)/devices/remove/(?P<devicepk>\d+)/$', views.pop_device_remove, name='pop_device_remove'),
    url(r'^internet/pop/(?P<poppk>\d+)/devices/add/(?P<devicepk>\d+)/$', views.pop_device_add, name='pop_device_add'),
# На Точках присутствия (апстиримы)
    url(r'^internet/pop/(?P<pk>\d+)/edit/upstreams/$', views.pop_upstreams, name='pop_upstreams'),
    url(r'^internet/pop/(?P<poppk>\d+)/upstreams/remove/(?P<corepk>\d+)/$', views.pop_upstreams_remove, name='pop_upstreams_remove'),
    url(r'^internet/pop/(?P<poppk>\d+)/upstreams/add/(?P<corepk>\d+)/$', views.pop_upstreams_add, name='pop_upstreams_add'),
# На Точках присутствия (даунстримы)
    url(r'^internet/pop/(?P<pk>\d+)/edit/downstreams/$', views.pop_downstreams, name='pop_downstreams'),
    url(r'^internet/pop/(?P<poppk>\d+)/downstreams/remove/(?P<customerpk>\d+)/$', views.pop_downstreams_remove, name='pop_downstreams_remove'),
    url(r'^internet/pop/(?P<poppk>\d+)/downstreams/add/(?P<customerpk>\d+)/$', views.pop_downstreams_add, name='pop_downstreams_add'),
# На Клиентах (апстримы)
    url(r'^internet/customer/(?P<pk>\d+)/edit/upstreams/$', views.customer_upstreams, name='customer_upstreams'),
    url(r'^internet/customer/(?P<customerpk>\d+)/upstreams/remove/(?P<poppk>\d+)/$', views.customer_upstreams_remove, name='customer_upstreams_remove'),
    url(r'^internet/customer/(?P<customerpk>\d+)/upstreams/add/(?P<poppk>\d+)/$', views.customer_upstreams_add, name='customer_upstreams_add'),

# Клиенты:
    url(r'^internet/customers/$', views.customer_list, name='customer_list'),
    url(r'^internet/customer/(?P<pk>\d+)/$', views.customer_detail, name='customer_detail'),
    url(r'^internet/customer/new/$', views.customer_new, name='customer_new'),
    url(r'^internet/customer/(?P<pk>\d+)/edit/$', views.customer_edit, name='customer_edit'),
    url(r'^internet/customer/(?P<pk>\d+)/remove/$', views.customer_remove, name='customer_remove'),
    url(r'^internet/customer/(?P<pk>\d+)/connection/$', views.customer_connection, name='customer_connection'),

#Оборудование:
    url(r'^inventory/pd/$', views.device_list, name='device_list'),
    url(r'^inventory/pd/(?P<pk>\d+)/$', views.device_detail, name='device_detail'),
    url(r'^inventory/pd/new/$', views.device_new, name='device_new'),
    url(r'^internet/pd/(?P<pk>\d+)/edit/$', views.device_edit, name='device_edit'),
    url(r'^internet/pd/(?P<pk>\d+)/remove/$', views.device_remove, name='device_remove'),

#IPv4
    url(r'^ipam/ipv4/$', views.ipv4_list, name='ipv4_list'),
    url(r'^ipam/ipv4/(?P<pk>\d+)/$', views.ipv4_detail, name='ipv4_detail'),
    url(r'^ipam/ipv4/new/$', views.ipv4_new, name='ipv4_new'),
    url(r'^ipam/ipv4/(?P<pk>\d+)/edit/$', views.ipv4_edit, name='ipv4_edit'),
    url(r'^ipam/ipv4/(?P<pk>\d+)/remove/$', views.ipv4_remove, name='ipv4_remove'),
    url(r'^ipam/ipv4/(?P<pk>\d+)/sepor/$', views.ipv4_sepor, name='ipv4_sepor'),


#Фильтры:
    url(r'^internet/filter/$', views.popfilter, name='popfilter'),
]
