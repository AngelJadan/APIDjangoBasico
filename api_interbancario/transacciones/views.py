from django.shortcuts import render
from .models import Cliente, Transaccion
from .serializers import ClienteSerializer, TransaccionSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

class get_depositos(ListAPIView):
    serializer_class = TransaccionSerializer
    
    def get_queryset(self):
        ced = self.kwargs["cedula"]
        tip = self.kwargs["tipo"]

        print("cedula",ced)
        client = Cliente.objects.filter(cedula = ced)
        cli = Cliente
        for clien in client:
            if clien.cedula == ced:
                print("Entro encontrado")
                cli.id = clien.id
                cli.cedula = clien.cedula
                cli.nombre = clien.nombre
                cli.apellido = clien.apellido
        print("Cliente ",cli.cedula)
        return Transaccion.objects.filter(cliente=cli.id,tipo=tip)