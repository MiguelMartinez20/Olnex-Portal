from django.contrib.auth.models import User
from .models import Employee
import django_filters

class EmployeeFilter(django_filters.FilterSet):
    
    name = django_filters.CharFilter(lookup_expr='icontains')
    lastname = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    position = django_filters.CharFilter(lookup_expr='icontains')
    birth_date = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Employee
        fields = ['rut', 'name', 'lastname', 'birth_date', 'address', 'position', 'salary']