from django.contrib import admin
from .models import Client, Medecin

# Register your models here.

admin.site.register(Client)
admin.site.register(Medecin)