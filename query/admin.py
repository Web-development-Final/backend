from django.contrib import admin
from .models import Event

admin.site.site_header = "Music Live"

admin.site.register(Event)
    