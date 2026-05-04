from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/<int:artwork_id>/', views.order_create, name='order_create'),
]