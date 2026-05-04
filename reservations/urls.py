from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('create/<int:event_id>/', views.reservation_create, name='reservation_create'),
    path('cancel/<int:pk>/', views.reservation_cancel, name='reservation_cancel'),
]