
from django.urls import path

from app_site import views
from api import views as apiViews

urlpatterns = [
    # rota, view responsável, site
    #projetopi.com
    path('',views.home,name='home'),   
    path('dashboard/',views.dashboard,name='dashboard'),   
    path('register/',views.register,name='register'),   
    path('v1/product',apiViews.apiProducts), #adicionar via post e listar via get
    path('v1/product/<id>', apiViews.apiProduct) #visualiza um especifico, atualiza e deleta
]
