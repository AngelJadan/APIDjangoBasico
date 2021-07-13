from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True, db_column="cli_id")
    cedula = models.CharField(max_length=20, blank=False, null=False, db_column="cli_cedula", unique=True)
    nombre = models.CharField(max_length=250, blank=False, null=False, db_column="cli_nombre")
    apellido = models.CharField(max_length=250, blank=False, null=False, db_column="cli_apellido")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return "Id:"+str(self.id)+" Cedula:"+str(self.cedula)

class Transaccion(models.Model):
    id = models.AutoField(primary_key=True, db_column="tra_id")
    fecha = models.DateField(db_column="tra_fecha", null=False, blank=False)
    valor = models.FloatField(db_column="tra_valor", null=False, blank=False)
    saldo_anterior = models.FloatField(db_column="tra_saldo_anterior", null=False, blank=False)
    saldo_actual = models.FloatField(db_column="tra_saldo_actual", null=False, blank=False)
    tipo = models.CharField(max_length=20, db_column="tra_tipo", null=False, blank=False, default="Deposito")
    cliente = models.ForeignKey(Cliente, db_column="tra_cli_id", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Transaccion"
        verbose_name_plural = "Transacciones"
    def __str__(self):
        return "Id:"+str(self.id)+" Cedula: "+str(self.cliente.cedula)+" Valor: "\
            +str(self.valor)+" Saldo anterior: "+str(self.saldo_anterior)+" Saldo actual: "+str(self.saldo_actual)\
                +" Tipo: "+str(self.tipo)

