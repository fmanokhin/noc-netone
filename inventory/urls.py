from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^internet/pops/$', views.pop_list, name='pop_list'),
]
