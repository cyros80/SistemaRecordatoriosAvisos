from .views import MyPasswordChangeView, MyPasswordResetDoneView 
from django.urls import path

app_name='pendientes'

urlpatterns = [

    path('change-password/',MyPasswordChangeView.as_view(),name='password-change-view'),
    path('change-password/done/', MyPasswordResetDoneView.as_view(),name='password-change-done'),
]