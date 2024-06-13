from peewee import *
from conexion import database


class user(Model):
    nombre = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    class Meta:
        database=database
        table_name = 'user'

class cliente(Model):
    id_cliente = AutoField(primary_key=True)
    nombre = CharField(max_length=50, unique=True)
    numero = CharField(max_length=50)
    direccion = CharField(max_length=50)
    colonia =CharField(max_length=50)
    estado = CharField(max_length=50)
    cp = IntegerField()
    pais = CharField(max_length=50)
    numero_pagos = IntegerField()
    orden_envio = IntegerField()
    
    def __str__(self):
        return self.nombre
    class Meta:
        database=database
        table_name = 'cliente'
        
class auto(Model):
    referencia = AutoField(primary_key=True)
    auto = CharField(max_length=50)
    modelo = IntegerField()
    version= CharField(max_length=50)
    color = CharField(max_length=50)
    precio = FloatField()
    transmision = CharField(max_length=100)
    motor = CharField(max_length=100)
    n_motor = IntegerField()
    n_puertas = IntegerField()
    tipo = CharField(max_length=50)
    chasis = CharField(max_length=50)
    fecha_aprovacion = IntegerField()
    certificado = IntegerField()
    
    def __str__(self):
        return self.auto
    class Meta:
        database=database
        table_name = 'auto'

    
    
    
    
class facturas(Model):
    id_factura= AutoField()
    referencia = ForeignKeyField(auto)
    auto = CharField(max_length=50)
    modelo = IntegerField()
    version= CharField(max_length=50)
    color = CharField(max_length=50)
    precio = FloatField()
    transmision = CharField(max_length=100)
    motor = CharField(max_length=100)
    n_motor = IntegerField()
    n_puertas = IntegerField()
    tipo = CharField(max_length=50)
    chasis = CharField(max_length=50)
    fecha_aprovacion = IntegerField()
    certificado = IntegerField()
    id_cliente = ForeignKeyField(cliente)
    nombre = CharField(max_length=50, unique=True)
    numero = CharField(max_length=50)
    Direccion = CharField(max_length=50)
    Colonia =CharField(max_length=50)
    Estado = CharField(max_length=50)
    CP = IntegerField()
    Pais = CharField(max_length=50)
    numero_pagos = IntegerField()
    orden_envio = IntegerField()
    fecha = CharField(max_length=59)
    hora = CharField(max_length=50)
    
    def __str__(self):
        return self.auto
    class Meta:
        database=database
        table_name = 'facturas'