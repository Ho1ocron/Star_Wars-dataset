from django.urls import path
from . import views

urlpatterns = [
    path('character/<int:character_id>/', views.get_character, name='get_character'),
    path('starship/<int:starship_id>/', views.get_starship, name='get_starship'),
    path('characters', views.get_characters, name='get_characters'),
    path('starships', views.get_starships, name='get_starships'),
]