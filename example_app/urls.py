from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bake', views.bake, name='bake'),
    path('ajax', views.ajax, name='ajax'),
    path('allauth', views.allauth, name='allauth'),
]