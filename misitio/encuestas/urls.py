from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('encuestas/', views.principal, name='principal'),
    path('contactenos/', views.contactenos, name='contactenos'),
]