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
# На Корах
    url(r'^internet/core/(?P<pk>\d+)/edit/downstreams/$', views.core_downstreams, name='core_downstreams'),
    url(r'^internet/core/(?P<corepk>\d+)/downstreams/remove/(?P<poppk>\d+)/$', views.core_downstreams_remove, name='core_downstreams_remove'),
    url(r'^internet/core/(?P<corepk>\d+)/downstreams/add/(?P<poppk>\d+)/$', views.core_downstreams_add, name='core_downstreams_add'),
# На Точках присутствия (апстиримы)
    url(r'^internet/pop/(?P<pk>\d+)/edit/downstreams/$', views.pop_downstreams, name='pop_downstreams'),
    url(r'^internet/pop/(?P<poppk>\d+)/downstreams/remove/(?P<corepk>\d+)/$', views.pop_downstreams_remove, name='pop_downstreams_remove'),
    url(r'^internet/pop/(?P<poppk>\d+)/downstreams/add/(?P<corepk>\d+)/$', views.pop_downstreams_add, name='pop_downstreams_add'),
]
