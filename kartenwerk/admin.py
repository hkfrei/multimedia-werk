from django.contrib import admin
from .models import Angebot, Referenz, Card, Preisplan, Preisplanfeature, Testimonial, Stakeholder, Blogpost, AngebotMessage

# Register your models here.
admin.site.register([Angebot, Referenz, Card,
                    Preisplan, Preisplanfeature, Testimonial, Stakeholder, Blogpost, AngebotMessage])
