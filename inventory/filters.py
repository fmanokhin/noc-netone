import django_filters
from .models import Pop

class PopFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='')
    class Meta:
        model = Pop
        fields = ['title',]
