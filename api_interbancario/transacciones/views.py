from django.shortcuts import render
from .models import Cliente, Transaccion
from .serializers import ClienteSerializer, TransaccionSerializer
from django.http.response import HttpResponse
from rest_framework.generics import ListAPIView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def depositar(request):
    if request.method == "POST":
        ced = request.POST["cedula"]
        monto = request.POST["monto"]
        fech = request.POST["fecha"]

        print("Cedula ",ced," monto ",monto," fecha ",fech)
        clie = Cliente.objects.filter(cedula=ced)
        print("Cliente ",clie)
        for c in clie:
            clie = c
        transacciones = Transaccion.objects.filter(cliente=clie)
        #print("Transacciones ",transacciones)
        saldo = 0
        print("Init saldo ",saldo)
        for tra in transacciones:
            saldo = tra.saldo_actual
            print("saldo ",saldo)

        n_saldo = saldo + float(monto)

        tran= Transaccion(fecha=fech,valor=monto, saldo_anterior=saldo, \
             saldo_actual=n_saldo,tipo="Deposito", cliente=clie)
        tran.save()

        print('saldo: ',saldo," monto: ",monto)
        print('Nuevo saldo: ',n_saldo)
        return HttpResponse("Se ha realizado el deposito exitosamente a la cuenta de "+
            ced+" por el monto de $"+str(monto))

@csrf_exempt
def retirar(request):
    if request.method == "POST":
        ced = request.POST["cedula"]
        monto = request.POST["monto"]
        fech = request.POST["fecha"]

        print("Cedula ",ced," monto ",monto," fecha ",fech)
        clie = Cliente.objects.filter(cedula=ced)
        print("Cliente ",clie)
        for c in clie:
            clie = c
        transacciones = Transaccion.objects.filter(cliente=clie)
        #print("Transacciones ",transacciones)
        saldo = 0
        print("Init saldo ",saldo)
        for tra in transacciones:
            saldo = tra.saldo_actual
            print("saldo ",saldo)

        if saldo>float(monto):
            n_saldo = saldo - float(monto)

            tran= Transaccion(fecha=fech,valor=monto, saldo_anterior=saldo, \
                saldo_actual=n_saldo,tipo="Retiro", cliente=clie)
            tran.save()

            print('saldo: ',saldo," monto: ",monto)
            print('Nuevo saldo: ',n_saldo)
            return HttpResponse("Se ha realizado el retiro exitosamente a la cuenta de "+
                ced+" por el monto de $"+str(monto))
        else:
            return HttpResponse("No cuenta con saldo suficiente para realizar el retiro.")
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