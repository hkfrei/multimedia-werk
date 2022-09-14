from django.db import models

# Create your models here.


class Angebot(models.Model):
    name = models.CharField(
        "Angebot Name", max_length=100, default="Angebotname")
    kurzbeschrieb = models.TextField("Kurzbeschrieb", default="Kurzbeschrieb")
    subtitel = models.TextField("Subtitel", default="Subtitel")
    video = models.CharField(
        'Video Name (aus static Ordner)', max_length=50, blank=True)
    cards = models.ManyToManyField("Card", blank=True)

    class Meta:
        verbose_name_plural = "Angebote"

    def __str__(self):
        return self.name


class Angebotbeispiel(models.Model):
    bildname = models.CharField("Bildname", max_length=50)
    titel = models.CharField("Title", max_length=100, default="Title")
    kurzbeschrieb = models.TextField("Kurzbeschrieb", default="Kurzbeschrieb")
    angebot = models.ForeignKey("Angebot", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Angebotsbeispiele"

    def __str__(self):
        return self.titel


class Card(models.Model):
    titel = models.CharField("Titel", max_length=100, default="Titel")
    kurzbeschrieb = models.TextField("Kurzbeschrieb", default="Kurzbeschrieb")
    subtitel = models.TextField("Subtitel", default="Subtitel")
    metadaten = models.TextField("Metadaten", blank=True)
    video = models.CharField('Video ID', max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Cards"

    def __str__(self):
        return self.titel
