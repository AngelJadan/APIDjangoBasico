from rest_framework import serializers
from .models import Cliente, Transaccion

class ClienteSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Cliente
        fields = (
            "id",
            'cedula',
            'nombre',
            'apellido'
        )

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = (
            'id',
            'fecha',
            'valor',
            'saldo_anterior',
            'saldo_actual',
            'tipo',
            'cliente',
        )