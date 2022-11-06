from django.contrib import admin

# Register your models here.
from notes_api.models import Note

admin.site.register(Note)