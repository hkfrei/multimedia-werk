from django.db import models

# Create your models here.


class Angebot(models.Model):
    name = models.CharField(
        "Angebot Name", max_length=100, default="Angebotname")
    subtitel = models.CharField("Subtitel", max_length=100, default="Subtitel")
    kurzbeschrieb = models.TextField("Kurzbeschrieb", default="Kurzbeschrieb")
    cards_titel = models.CharField(
        "Angebot Cards Titel", max_length=100, default="Angebot Cards Titel")
    cards_beschrieb = models.TextField(
        "Angebot Cards Beschrieb", default="Angebot Cards Beschrieb")
    video = models.CharField(
        'Video Name (aus static Ordner)', max_length=50, blank=True)
    bild = models.CharField("Bild", max_length=100, default="gis.webp")
    cards = models.ManyToManyField("Card", blank=True)
    preise = models.ManyToManyField("Preisplan", blank=True)

    class Meta:
        verbose_name_plural = "Angebote"

    def __str__(self):
        return self.name


class Angebotbeispiel(models.Model):
    titel = models.CharField("Title", max_length=100, default="Title")
    kurzbeschrieb = models.TextField("Kurzbeschrieb", default="Kurzbeschrieb")
    bild = models.CharField("Bildname", max_length=50)
    angebot = models.ForeignKey("Angebot", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Angebotsbeispiele"

    def __str__(self):
        return self.titel


class Card(models.Model):
    titel = models.CharField("Titel", max_length=100, default="Titel")
    subtitel = models.TextField("Subtitel", default="Subtitel")
    metadaten = models.TextField("Metadaten", blank=True)
    kurzbeschrieb = models.TextField("Kurzbeschrieb", default="Kurzbeschrieb")
    video = models.CharField('Video ID', max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Cards"

    def __str__(self):
        return self.titel


class Preisplan(models.Model):
    order = models.IntegerField("Order", default=1)
    name = models.CharField("Name", max_length=50, default="Preisplan Name")
    preis = models.CharField("Preis", max_length=50)
    einheit = models.CharField("Einheit", max_length=50)
    popular = models.BooleanField("Populär", default=False)
    features = models.ManyToManyField("Preisplanfeature", blank=True)

    class Meta:
        verbose_name_plural = "Preispläne"
        ordering = ['order']

    def __str__(self):
        return self.name


class Preisplanfeature(models.Model):
    name = models.CharField("Titel", max_length=100)
    aktiv = models.BooleanField("Aktiv", default=True)

    class Meta:
        verbose_name_plural = "Preisplan Features"

    def __str__(self):
        return self.name + " | aktiv = " + str(self.aktiv)
