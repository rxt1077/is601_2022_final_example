from django.urls import path

from . import views

urlpatterns = [
    path('', views.order_form, name='order'),
    path('info/<int:id>', views.order_info, name='info'),
]