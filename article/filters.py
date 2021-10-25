import django_filters
from .models import Article_Info


class articleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    small_description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Article_Info
        fields = ['title', 'small_description',  'type_section']
