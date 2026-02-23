from django.forms import ModelForm,forms
from django import forms
from .models import *


class ordenar(ModelForm):

    class Meta:
        model = Orden
        fields ='__all__'
        exclude=['DELETE']
class clienteform(ModelForm):

    class Meta:
        model = Cliente
        fields ='__all__'
        #exclude=['cliente']
class tagform(ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'
class productoform(ModelForm):

    class Meta:
        model = Inventario1
        fields ='__all__'
        #exclude=['cliente']
class proveedorform(ModelForm):

    class Meta:
        model = Proveedor
        fields ='__all__'
        #exclude=['cliente']
class empleadoform(ModelForm):

    class Meta:
        model = Empleado
        fields ='__all__'
        #exclude=['cliente']
class devolucionform(forms.Form):


    def __init__(self,*args,**kwargs):
        self.pk=args[0]
        args=args[1:]
        self.opciones=[]
        self.ordens=Orden.objects.filter(cliente__idc=self.pk)
        for i in self.ordens:
            if i.estado=='Enviado':
                self.opciones.append((i.id,i.producto))

        self.opciones=tuple(self.opciones)
        super(devolucionform,self).__init__( *args,**kwargs)
        self.fields['producto'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=self.opciones)



