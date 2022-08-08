from django.db import models

# Create your models here.


class Angebot(models.Model):
    name = models.CharField("Angebot Name", max_length=100)
    kurzbeschrieb = models.TextField("Kurzbeschrieb")
    bild = models.CharField('Bildname', max_length=50)

    class Meta:
        verbose_name_plural = "Angebote"

    def __str__(self):
        return self.name
