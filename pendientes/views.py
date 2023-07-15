from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from .forms import PendientesForm
from .models import Pendientes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django import template
from django.http import HttpResponseRedirect
from .decorators import custom_login_required
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView

register = template.Library()  



# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView

class MyPasswordChangeView(PasswordChangeView):
    template_name='registration/password-change.html'
    success_url=reverse_lazy('users:password-change-done-view')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name='registration/password-reset-done.html'

@login_required
@custom_login_required
def home (request):
    return render (request, 'pendientes/home.html')

@login_required
def index(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name=="Academica":
        return HttpResponseRedirect(reverse('peticionese'))
    elif group.name=="Administracion":
        return HttpResponseRedirect(reverse('peticionesp'))
    elif group.name=="Planeacion":
        return HttpResponseRedirect(reverse('peticionesf'))
    elif group.name=="Direccion":
        return HttpResponseRedirect(reverse('enviar'))

    context = {}
    template = "pendientes/home.html"
    return render(request, template, context)



def consultaPendiente(request, id):
    pendiente=Pendientes.objects.get(id=id)

    return render(request,"pendientes/editarPendiente.html",{'pendiente':pendiente})

def group_required(*group_names):
   """ Evalua si el usuario pertenece a alguno de los grupos indicados."""

   def in_groups(u):
       if u.is_authenticated:
           if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
               return True
       return False
   return user_passes_test(in_groups)


def editar_pendiente(request):
    id=int(request.POST['id'])
    area =request.POST['Area']
    tarea=request.POST['tarea']
    porcentaje=request.POST['porcentaje']
    estado=request.POST['estado']

    pendiente=Pendientes.objects.get(id=id)
    pendiente.Area=area
    pendiente.tarea=tarea
    pendiente.porcentaje=porcentaje
    pendiente.estado=estado

    pendiente.save()

    return redirect('/')

def editar_pendiente2(request):
    id=int(request.POST['id'])
    area =request.POST['Area']
    tarea=request.POST['tarea']
    

    pendiente=Pendientes.objects.get(id=id)
    pendiente.Area=area
    pendiente.tarea=tarea
    

    pendiente.save()

    return redirect('/')

def editar(request,id,):
    pendiente= get_object_or_404(Pendientes,id=id)
    return render(request,"pendientes/editarpendiente.html",{'pendiente':pendiente}) 

def editar2(request,id,):
    pendiente= get_object_or_404(Pendientes,id=id)
    return render(request,"pendientes/editarpendiente2.html",{'pendiente':pendiente})

def editar3(request,id,):
    pendientes= get_object_or_404(Pendientes,id=id)
    return render(request,"pendientes/editarpendiente3.html",{'pendientes':pendientes})          

def editarPendiente(request, id):
    pendiente2=get_object_or_404(Pendientes,id=id)
    form= PendientesForm(request.POST, instance=pendiente2)

    if form.is_valid():
        form.save()
        pendientes=Pendientes.objects.all()
        return render(request,"pendientes/home.html",{'pendientes':pendientes})
    

    return render(request,"pendientes/editarPendiente.html",{'pendiente':pendiente2})


def exit(request):
    logout(request)
    return redirect('home')


def register(request):
    data ={
        'form':CustomUserCreationForm()
    }

    if request.method =='POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            user=authenticate(username=user_creation_form.cleaned_data['username'],password=user_creation_form.cleaned_data['password1'],groups=user_creation_form.cleaned_data['groups'])
            login(request,user)

            return redirect('exit')

    return render(request, 'registration/register.html', data)

@login_required
@custom_login_required
def enviar(request):
    pendientes_form=PendientesForm()
    if request.method == 'POST':
        pendientes_form=PendientesForm(data=request.POST)

        if pendientes_form.is_valid():
            pendientes_form.save()
            return redirect(reverse('enviar')+'?ok')
        else:
            return redirect(reverse('enviar')+'?error')

    return render(request,'pendientes/home.html',{'form':pendientes_form})

def eliminarPendiente(request,id,confirmacion='pendientes/confirmar.html'):
    pendiente= get_object_or_404(Pendientes,id=id)
    if request.method=='POST':
        pendiente.delete()
        pendientes=Pendientes.objects.all()
        return redirect('/')
    return render(request,confirmacion,{'object':pendiente})
    
    


@login_required
@custom_login_required
@group_required('Administracion','Direccion',)
def tareasadmin(request):
    peticionesp=Pendientes.objects.filter(Area="SubAdministrativa",estado="Pendiente")
    peticionese=Pendientes.objects.filter(Area="SubAdministrativa",estado="En Proceso")
    peticionesf=Pendientes.objects.filter(Area="SubAdministrativa",estado="Finalizada")

    return render(request,'pendientes/tareasadmin.html',{"peticionesp":peticionesp,"peticionese":peticionese,"peticionesf":peticionesf})

@login_required
@group_required('Academica','Direccion')
def petcionese(request):
    peticionesp=Pendientes.objects.filter(Area="SubAcademica",estado="Pendiente")
    peticionese=Pendientes.objects.filter(Area="SubAcademica",estado="En Proceso")
    peticionesf=Pendientes.objects.filter(Area="SubAcademica",estado="Finalizada")

    return render(request,'pendientes/tareasaced.html',{"peticionesp":peticionesp,"peticionese":peticionese,"peticionesf":peticionesf})

@login_required
@group_required('Planeacion','Direccion')
def petcionesf(request):
    peticionesp=Pendientes.objects.filter(Area="SubPlaneacion",estado="Pendiente")
    peticionese=Pendientes.objects.filter(Area="SubPlaneacion",estado="En Proceso")
    peticionesf=Pendientes.objects.filter(Area="SubPlaneacion",estado="Finalizada")

    return render(request,'pendientes/tareasplan.html',{"peticionesp":peticionesp,"peticionese":peticionese,"peticionesf":peticionesf})


@login_required
@group_required('Direccion')
def todas(request):
    peticionesp=Pendientes.objects.filter(estado="Pendiente")
    peticionese=Pendientes.objects.filter(estado="En Proceso")
    peticionesf=Pendientes.objects.filter(estado="Finalizada")

    return render(request,'pendientes/todas.html',{"peticionesf":peticionesf,"peticionese":peticionese,"peticionesp":peticionesp})

