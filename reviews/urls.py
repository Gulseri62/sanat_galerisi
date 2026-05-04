from django.urls import path
from . import views

urlpatterns = [
    path('review/artwork/<int:artwork_id>/', views.add_review, {'event_id': None}, name='add_artwork_review'),
    path('review/event/<int:event_id>/', views.add_review, {'artwork_id': None}, name='add_event_review'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('favorites/add/<int:artwork_id>/', views.add_favorite, name='add_favorite'),
    path('favorites/remove/<int:artwork_id>/', views.remove_favorite, name='remove_favorite'),
    path('support/', views.support_ticket_create, name='support_ticket'),
]