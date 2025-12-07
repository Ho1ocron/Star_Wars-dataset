from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Character, Starship
from .utils import get_character_from_swapi, get_starship_from_swapi


def get_characters(request: HttpRequest) -> HttpResponse:
    characters = Character.objects.all()
    return render(request, "characters_list.html", {"characters": characters})


def get_character(request: HttpRequest, character_id: int) -> HttpResponse:
    try:
        character = Character.objects.get(id=character_id)
    except Character.DoesNotExist:
        character = get_character_from_swapi(character_id)

    return render(request, 'character.html', {'character': character})


def get_starships(request: HttpRequest) -> HttpResponse:
    starships = Starship.objects.all()
    return render(request, 'starship_list.html', {'starships': starships})


def get_starship(request: HttpRequest, starship_id: int) -> HttpResponse:
    try:
        starship = Starship.objects.get(id=starship_id)
    except Starship.DoesNotExist:
        try:
            starship = get_starship_from_swapi(starship_id)
        except:
            return HttpResponse("Starship not found", status=404)

    return render(request, 'starship.html', {'starship': starship})