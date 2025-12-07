from django.contrib import admin

# Register your models here.
# s@sts.s.ru

from .models import Character, Starship


admin.site.register(Character)
admin.site.register(Starship)


class ImperialSiteAdmin(admin.AdminSite):
    list_display = (
        "title",
        "description",
        "is_published",
        "is_on_main",
        "category",
        "wrapper"
    )

    list_editable = (
        "is_published",
        "is_on_main",
        "category",
    )

    searh_fields = ("title")
    list_filter = ("category")
    list_display_links = ("title",)


class StarshipInline(admin.StackedInline):
    model = Starship
    extra = 0


class ImperialCharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "category")
    list_editable = ("is_published", "category")
    search_fields = ("name",)
    list_filter = ("category",)
    list_display_links = ("name",)


class CharacterInline(admin.ModelAdmin):
    inlines = (StarshipInline)
    list_display = (
        "name",
    )
