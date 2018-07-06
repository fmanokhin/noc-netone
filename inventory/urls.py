from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pop_list, name='pop_list'),
]
