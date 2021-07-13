from django.contrib import admin
from django.contrib.admin.helpers import AdminForm
from .models import * 
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Transaccion)