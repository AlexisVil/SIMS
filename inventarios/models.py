from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Inventario(models.Model):
    iccid = models.IntegerField(primary_key=True)
    marca = models.IntegerField(null=False)
    dn = models.IntegerField(null=False)
    preactivacion = models.IntegerField(null=True, default=0)
    fecha_activ = models.DateTimeField(null=True, blank=True)
    venta = models.IntegerField(null=True, blank=True)
    idVenta = models.IntegerField(null=True, blank=True)
    fecha_venta = models.DateTimeField(null=True, blank=True)
    fecha_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ICCID: ' + str(self.iccid) + ' ' + 'DN: ' + str(self.dn) + ' ' + 'Marca: ' + str(self.marca)


class Marca(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id_marca) + '-' + self.nombre


class Sucursal(models.Model):
    id_sucursal = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False)
    id_padresucursal = models.IntegerField(null=True, blank=True)
    fecha_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'sucursal: ' + str(self.id_sucursal) + '-' + self.nombre


class Traslado(models.Model):
    id_traslado = models.IntegerField(primary_key=True)
    sucursal_origen = models.IntegerField(null=True, blank=True)
    sucursal_destino = models.IntegerField(null=True, blank=True)
    estatus = models.CharField(max_length=200, blank=True, null=True)
    fecha_reg = models.DateTimeField(auto_now_add=True)
    fecha_recepcion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'id_traslado: ' + str(self.id_traslado) + self.estatus


class Ventas(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha_reg = models.DateTimeField(auto_now_add=True)
