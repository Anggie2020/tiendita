from django.db import models

# Create your models here.

class inicioSesion(models.Model):
    idSesion=models.AutoField(null=False,primary_key=True)    
    fecha=models.CharField(max_length=30,null=False)
    hora=models.CharField(max_length=30,null=False)
    descripcion=models.CharField(max_length=30,null=False)

class movimientos(models.Model):
    idMovimiento=models.AutoField(null=False,primary_key=True)   
    tipoMovimiento=models.CharField(max_length=30,null=False)
    cantidadProducto=models.CharField(max_length=30,null=False)
    descripcion=models.CharField(max_length=30,null=False)
    fecha=models.CharField(max_length=30,null=False)
    hora=models.CharField(max_length=30,null=False)
    valorTotal=models.CharField(max_length=30,null=False)

class producto(models.Model):
    idProducto=models.AutoField(null=False,primary_key=True)   
    nombreProducto=models.CharField(max_length=30,null=False)
    stockActual=models.CharField(max_length=30,null=False)
    stockMinimo=models.CharField(max_length=30,null=False)
    valorUnitario=models.CharField(max_length=30,null=False)
    categoria=models.CharField(max_length=30,null=False)
    
    def _str_(self):
        return self.nombreProducto

class tienda(models.Model):
    idTienda=models.AutoField(null=False,primary_key=True)   
    nombre=models.CharField(max_length=30,null=False)
    direccion=models.CharField(max_length=60,null=False)
    
    def _str_(self):
        return self.nombre
    
class usuario(models.Model):
    idUsuario=models.AutoField(null=False,primary_key=True)   
    nombre=models.CharField(max_length=30,null=False)
    password=models.CharField(max_length=30,null=False)
    tienda=models.CharField(max_length=30,null=False)