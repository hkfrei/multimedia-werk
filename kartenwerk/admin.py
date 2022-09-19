from django.contrib import admin
from .models import Angebot, Referenz, Card, Preisplan, Preisplanfeature, Testimonial, Stakeholder, Blogpost

# Register your models here.
admin.site.register([Angebot, Referenz, Card,
                    Preisplan, Preisplanfeature, Testimonial, Stakeholder, Blogpost])
