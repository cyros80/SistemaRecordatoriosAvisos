from django.contrib import admin
from .models import Pendientes, Profile

# Register your models here.
class AdministradorModelo(admin.ModelAdmin):
  
    list_display=('Area','tarea','estado','created','updated')


admin.site.register(Pendientes,AdministradorModelo)

class Perfil(admin.ModelAdmin):
    list_display= ('user','id' )



admin.site.register(Profile,Perfil)