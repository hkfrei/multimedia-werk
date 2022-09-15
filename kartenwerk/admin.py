from django.contrib import admin
from .models import Angebot, Angebotbeispiel, Card, Preisplan, Preisplanfeature

# Register your models here.
admin.site.register([Angebot, Angebotbeispiel, Card,
                    Preisplan, Preisplanfeature])
