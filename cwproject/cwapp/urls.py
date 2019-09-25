from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addbooks/', views.addBook),
    path('all/', views.all),
    path('allYear/',views.allYear)
]