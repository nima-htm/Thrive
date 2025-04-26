from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.advisor_list, name='advisor_list'),
    path('signup/', views.user_sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('advisor/dashboard/', views.advisor_dashboard, name='advisor_dashboard'),
]