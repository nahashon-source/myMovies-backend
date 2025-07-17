from django.contrib import admin
from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'release_year', 'created_at')
    list_filter = ('category', 'release_year')
    search_fields = ('title', 'description')