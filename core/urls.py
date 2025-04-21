from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-to-list', views.index, name='add-to-list')
]