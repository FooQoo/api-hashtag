from django.contrib import admin
from .models import Hashtag, Tweet, Word, Biterm, CoOccurrence


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass


@admin.register(Biterm)
class BitermAdmin(admin.ModelAdmin):
    pass


@admin.register(Tweet)
class BitermAdmin(admin.ModelAdmin):
    pass


@admin.register(CoOccurrence)
class CoOccurrenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    pass
