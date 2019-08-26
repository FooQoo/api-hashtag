from django.contrib import admin
from .models import Hashtag, HashtagTask, Word, Biterm, CoOccurrence


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass


@admin.register(Biterm)
class BitermAdmin(admin.ModelAdmin):
    pass


@admin.register(CoOccurrence)
class CoOccurrenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    pass


@admin.register(HashtagTask)
class HashtagTaskAdmin(admin.ModelAdmin):
    pass
