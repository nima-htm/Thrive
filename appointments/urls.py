from django.urls import path
from . import views
app_name = 'appointments'
urlpatterns = [
    path('', views.appointments_list, name='appointments_list'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
]