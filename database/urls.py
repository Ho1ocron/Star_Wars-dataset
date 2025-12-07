from django.urls import path
from . import views

urlpatterns = [
    path('person/<int:person_id>/', views.get_character, name='get_person'),
    path('starship/<int:starship_id>/', views.get_starship, name='get_starship'),
    path('people', views.get_characters, name='get_people'),
    path('starships', views.get_starships, name='get_starships'),
]