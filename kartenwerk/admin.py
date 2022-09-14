from django.contrib import admin
from .models import Angebot, Angebotbeispiel, Card

# Register your models here.
admin.site.register([Angebot, Angebotbeispiel, Card])
