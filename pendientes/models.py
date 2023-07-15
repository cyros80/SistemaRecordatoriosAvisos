from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="ID")
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Pendientes(models.Model):
    id= models.AutoField(primary_key=True,verbose_name="Folio")
    os_choices={
        ('SubAdministrativa','SubAdministrativa'),
        ('SubPlaneacion','SubPlaneacion'),
        ('SubAcademica','SubAcademica')
    }
    os_choices2={
        ('Pendiente','Pendiente'),
        ('En Proceso','En Proceso'),
        ('Finalizada','Finalizada')
    }
    os_choices3={
        ('0%','0%'),
        ('25%','25%'),
        ('50%','50%'),
        ('75%','75%')
    }
    Area=models.CharField(max_length=30,choices=os_choices,verbose_name="Area")
    tarea=models.TextField(max_length=200,verbose_name="Tarea")
    porcentaje=models.CharField(max_length=10,choices=os_choices3,default="0%",verbose_name="Porcentaje")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Asignacion")
    updated=models.DateTimeField(auto_now_add=True,verbose_name="Conclusion")
    estado=models.CharField(max_length=25,default="Pendiente",choices=os_choices2,verbose_name="Estado")

    class Meta:
        verbose_name= "Pendientes"
        verbose_name_plural= "Pendientes"
        ordering= ["-created"]

    def __str__(self):
        return self.Area
    

  
