
from django.urls import path

from app_site import views

urlpatterns = [
    # rota, view responsável, site
    #projetopi.com
    path('',views.home,name='home'),   
    path('dashboard/',views.dashboard,name='dashboard'),   
    path('register/',views.register,name='register'),   
]
