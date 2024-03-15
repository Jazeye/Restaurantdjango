from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservationtablepage/', views.reservationtable_view, name='reservationtable_page'),
    path('menu/', views.menu_view, name='menu_page'),
]

