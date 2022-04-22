import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class OrdenFilter(django_filters.FilterSet):
    producto = django_filters.CharFilter(label='Id producto',field_name="producto")
    estado = django_filters.ChoiceFilter(choices=ESTADO)
    fechadsd = DateFilter(label='Desde',field_name="fecha", lookup_expr='gte')
    fechahst = DateFilter(label='Hasta',field_name="fecha", lookup_expr='lte')
    note = CharFilter(label='Nota',field_name='nota',lookup_expr='icontains')
    class Meta:
        model: Orden
        fields='__all__'

class ProductosFiltro(django_filters.FilterSet):
    codigo= django_filters.CharFilter(field_name='codigo')
    descripcion= django_filters.CharFilter(label='Descripcion',field_name='descripcion',lookup_expr='icontains')
    categoria= django_filters.ChoiceFilter(field_name='categoria',choices=CATEGORY)

    class Meta:
        model: Inventario1
        fields='__all__'


class ProveedoresFiltro(django_filters.FilterSet):
    id= django_filters.CharFilter(field_name='idp')
    nombre= django_filters.CharFilter(field_name='nombre')
    sector = django_filters.CharFilter(field_name='sector')
    telefono= django_filters.CharFilter(field_name='telefono')

    class Meta:
        model: Proveedor
        fields = '__all__'
class ClientesFiltro(django_filters.FilterSet):
    id= django_filters.CharFilter(field_name='idc')
    nombre= django_filters.CharFilter(field_name='nombre')
    correo = django_filters.CharFilter(field_name='correo')
    cedula= django_filters.CharFilter(field_name='cedula')

    class Meta:
        model: Cliente
        fields = '__all__'


class EmpleadosFiltro(django_filters.FilterSet):
    numero=django_filters.CharFilter(field_name='numemp',label='Empleado Numero')
    nombre = django_filters.CharFilter(field_name='nombre')
    apellido=django_filters.CharFilter(field_name='apellido')
    deptno= django_filters.NumberFilter(label='Numero dept')
    cargo=django_filters.CharFilter(field_name='cargo')
    salariomn=django_filters.NumberFilter(field_name='salario',label='Salario mayor que', lookup_expr='gte')
    salariomy = django_filters.NumberFilter(field_name='salario', label='Salario menor que', lookup_expr='lte')
    class Meta:
        model: Empleado
        fields = '__all__'