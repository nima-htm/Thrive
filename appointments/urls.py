from django.urls import path
from . import views
app_name = 'appointments'
urlpatterns = [
    path('', views.appointments, name='appointments'),
]