"""tareas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import home, enviar, petcionese,petcionesf,tareasadmin, exit,register,todas,editar,editar_pendiente,eliminarPendiente, index
from .views import editar2, editar_pendiente, editar3,editar_pendiente2, MyPasswordChangeView,MyPasswordResetDoneView



urlpatterns = [

    path('', index, name='home'),
    path('enviar/', enviar, name='enviar'),
    path('peticionesadmin/',tareasadmin, name='peticionesp'),
    path('peticionesacede/',petcionese, name='peticionese'),
    path('peticionesplan/',petcionesf, name='peticionesf'),
    path('todas/',todas, name='todas'),
    path('logout/', exit,name='exit'),
    path('register/', register,name='register'),
    
    path('editarPendinete/<int:id>',editar,name='editar'),
    path('editarPendinete2/<int:id>',editar2,name='editar2'),
    path('editarPendinete3/<int:id>',editar3,name='editar3'),
    path('editarPendiente/',editar_pendiente,name='editarPendiente'),
    path('editarPendiente2/',editar_pendiente2,name='editarPendiente2'),
    path('eliminar/<int:id>',eliminarPendiente,name='eliminar'),
    path('change-password/',MyPasswordChangeView.as_view(),name='password-change-view'),
    path('change-password/done/', MyPasswordResetDoneView.as_view(),name='password-change-done')
]
