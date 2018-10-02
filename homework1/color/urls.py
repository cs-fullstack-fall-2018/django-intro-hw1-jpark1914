from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bluefire/<str:color>/', views.picker, name='bluefire')
]