from django.db import models

# Create your models here.
class Tag(models.Model):

    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
CATEGORY=(('Comesticos','Comesticos'),('Prendas','Prendas'),('Calzado','Calzado'))
class Proveedor(models.Model):
    idp=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    correo=models.EmailField(blank=True, null=True)
    sector = models.CharField(max_length=50)
    nombrecontac=models.CharField(max_length=50)
    telefono = models.BigIntegerField()

    def __str__(self):
        return self.nombre
class Inventario1(models.Model):


    codigo= models.CharField(max_length=5)
    descripcion = models.CharField(max_length=50, blank=True)
    categoria = models.CharField(max_length=50, null=True, choices=CATEGORY)
    precio= models.FloatField( null=True)
    stocki= models.IntegerField()
    entradas=models.IntegerField()
    salidas=models.IntegerField()
    tags = models.ManyToManyField(Tag)

    idp= models.ForeignKey(Proveedor,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion


    def _get_stockf(self):
        return (self.stocki+self.entradas)-self.salidas
    stockf= property(_get_stockf)

    def _get_precioitbis(self):
        return self.precio + self.precio*0.18
    precioitbis= property(_get_precioitbis)

class Empleado(models.Model):
    numemp=models.AutoField(primary_key=True)
    clave= models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    deptno = models.IntegerField()
    correo=models.EmailField(max_length=50,null=True)
    cargo=models.CharField(max_length=50)
    salario=  models.BigIntegerField(null=True)

    def _get_salarioitbis(self):
        return self.salario - self.salario*0.18
    salarioitbis= property(_get_salarioitbis)



class Cliente(models.Model):
    idc=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)
    direccion=models.CharField(max_length=50)
    correo=models.EmailField(blank=True, null=True)
    telefono=models.BigIntegerField()
    cedula=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
DETALLES=(('Compra','Compra'),('Devolucion','Devolucion'))
ESTADO = (
        ('Pendiente', 'Pendiente'),
        ('En camino', 'En camino'),
        ('Enviado', 'Enviado')
    )

class Orden(models.Model):

    idf = models.IntegerField(default=0 )
    cliente= models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    producto= models.ForeignKey(Inventario1, null=True, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True,default=0)
    fecha=  models.DateTimeField(auto_now_add=True, null=True)
    estado = models.CharField(max_length=200, null=True, choices=ESTADO)
    nota = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.producto.descripcion


class Diario(models.Model):
    idf = models.ForeignKey(Orden,default=0,on_delete=models.CASCADE)


    fecha=  models.DateTimeField(auto_now_add=True, null=True)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    detalle = models.CharField(max_length=50,null=True, choices=DETALLES)
    debito = models.FloatField(null=True)
    credito = models.FloatField(null=True)
    def __str__(self):
        return self.cliente.idc


class Historial(models.Model):
    numemp=models.IntegerField(null=True)
    fecha= models.DateTimeField(auto_now_add=True ,null=True)




