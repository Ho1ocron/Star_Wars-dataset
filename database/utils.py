from httpx import Client

from .models import Character, Starship


def get_starship_from_swapi(starship_id: int) -> Starship:
    url = f"https://swapi.dev/api/starships/{starship_id}/"
    with Client() as client:
        response = client.get(url)
        response.raise_for_status()
        data: dict = response.json()

    starship = Starship.objects.create(
        id=starship_id,
        name=data['name'],
        model=data['model'],
        manufacturere=data['manufacturer'],
        cost_in_credits=data['cost_in_credits'],
        length=data['length'],
        max_atmosphering_speed=data['max_atmosphering_speed'],
        crew=data['crew'],
        passengers=data['passengers'],
        cargo_capacity=data['cargo_capacity'],
        consumables=data['consumables'],
        hyperdrive_rating=data['hyperdrive_rating'],
        MGLT=data['MGLT'],
        starship_class=data['starship_class'],
    )

    starship.save()
    return starship


def get_character_from_swapi(character_id: int) -> Character:
    url = f"https://swapi.dev/api/people/{character_id}/"
    with Client() as client:
        response = client.get(url)
        response.raise_for_status()
        data: dict = response.json()

    character = Character.objects.create(
        id=character_id,
        name=data['name'],
        birth_year=data['birth_year'],
        eye_color=data['eye_color'],
        gender=data['gender'],
        hair_color=data['hair_color'],
        height=data['height'],
        mass=data['mass'],
        skin_color=data['skin_color'],
        homeworld=data["homeworld"],
        species=",".join(data.get("species", [])) or "unknown",
    )

    character.save()

    for starship_url in data.get('starships', []):
        starship_id = int(starship_url.rstrip('/').split('/')[-1])
        try:
            starship = Starship.objects.get(id=starship_id)
        except Starship.DoesNotExist:
            starship = get_starship_from_swapi(starship_id)

        character.starships.add(starship)

    character.save()
    return character

