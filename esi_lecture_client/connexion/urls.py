from django.urls import path
from . import views

app_name = 'connexion'
urlpatterns = [
    path('', views.connexion, name='connexion'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    ]