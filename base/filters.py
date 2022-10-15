import django_filters
from django_filters import DateFilter
from .models import *
class crudstFilter(django_filters.FilterSet):
    class Meta:
        model = crudst
        fields ='__all__'
        exclude =['email','address']
