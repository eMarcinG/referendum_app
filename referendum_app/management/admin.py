from django.contrib import admin
from .models import Author, Idea

# Rejestracja modeli w panelu admina
admin.site.register(Author)
admin.site.register(Idea)