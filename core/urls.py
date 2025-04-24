from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('advisor_list/',views.advisor_list,name='advisor_list')
]