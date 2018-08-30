import django_filters
from .models import Pop, Core, Customer, Device

class PopFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='')
    class Meta:
        model = Pop
        fields = ['title',]

class CoreFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='')
    class Meta:
        model = Core
        fields = ['title',]

class CustomerFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='')
    class Meta:
        model = Customer
        fields = ['title',]

class DeviceFilter(django_filters.FilterSet):
    dnsname = django_filters.CharFilter(lookup_expr='icontains', label='')
    class Meta:
        model = Device
        fields = ['dnsname',]
