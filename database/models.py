from django.db.models import (
    Model,
    IntegerField,
    IntegerField,
    CharField,
    ImageField,
    ManyToManyField,
    ManyToManyRel
)


class Character(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=100)
    mass = IntegerField()
    hair_color = CharField(max_length=100)
    skin_color = CharField(max_length=100)
    eye_color = CharField(max_length=100)
    birth_year = CharField(max_length=100)
    gender = CharField(max_length=100)
    homeworld = CharField(max_length=100)
    species = CharField(max_length=100)
    starships = ManyToManyField("models.Starship", related_name="characters_starships")

    def __str__(self) -> str:
        return f"Model id: {self.id}, model name: {self.name}."

    class Meta:
        table = "characters"


class Starship(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=100)
    model = CharField(max_length=100)
    manufacturere = CharField(max_length=100)
    cost_in_credits = CharField(max_length=100)
    length = CharField(max_length=100)
    max_atmosphering_speed = CharField(max_length=100)
    crew = CharField(max_length=100)
    passengers = CharField(max_length=100)
    cargo_capacity = CharField(max_length=100)
    consumables = CharField(max_length=100)
    hyperdrive_rating = CharField(max_length=100)
    MGLT = CharField(max_length=100)
    starship_class = CharField(max_length=100)