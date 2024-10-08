from django.contrib import admin
from .models import Book, Genres

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
