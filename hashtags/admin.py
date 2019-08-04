from django.contrib import admin
from .models import Hashtag, SearchTask


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    pass


@admin.register(SearchTask)
class SearchTaskAdmin(admin.ModelAdmin):
    pass
