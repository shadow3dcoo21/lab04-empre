from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('autor/<int:id_autor>/', views.entradas_por_autor, name='entradas_por_autor'),
]

