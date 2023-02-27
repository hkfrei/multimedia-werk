from django.db import models

# Create your models here.


class Angebot(models.Model):
    order = models.IntegerField("Order", default=1)
    name = models.CharField(
        "Angebot Name", max_length=100, default="Angebotname")
    subtitel = models.CharField("Subtitel", max_length=100, default="Subtitel")
    kurzbeschrieb = models.TextField("Kurzbeschrieb", default="Kurzbeschrieb")
    bild = models.CharField("Bild", max_length=100, default="gis.webp")
    video = models.CharField(
        'Video Name (aus static Ordner)', max_length=50, blank=True)
    cards_titel = models.CharField(
        "Angebot Cards Titel", max_length=100, default="Angebot Cards Titel")
    cards_beschrieb = models.TextField(
        "Angebot Cards Beschrieb", default="Angebot Cards Beschrieb")
    cards = models.ManyToManyField("Card", blank=True)
    preise = models.ManyToManyField("Preisplan", blank=True)

    class Meta:
        verbose_name_plural = "Angebote"
        ordering = ["order"]

    def __str__(self):
        return self.name


class Referenz(models.Model):
    titel = models.CharField("Titel", max_length=100, default="Title")
    kurzbeschrieb = models.TextField("Kurzbeschrieb", default="Kurzbeschrieb")
    bild = models.CharField("Bild", max_length=50, blank=True)
    video = models.CharField("Video ID", max_length=50, blank=True)
    angebot = models.ForeignKey("Angebot", on_delete=models.CASCADE)
    stakeholder = models.ForeignKey(
        "Stakeholder", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Referenzen"

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


class Testimonial(models.Model):
    text = models.TextField("Testimonial Text")
    angebot = models.ForeignKey("Angebot", on_delete=models.CASCADE)
    stakeholder = models.ForeignKey(
        "Stakeholder", on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.text


class Stakeholder(models.Model):
    logo = models.CharField("Logo", max_length=100)
    firma = models.CharField("Firma", max_length=100)
    name = models.CharField("Name", max_length=50)
    vorname = models.CharField("Vorname", max_length=50)
    position = models.CharField("Position", max_length=100)

    class Meta:
        verbose_name_plural = "Stakeholders"

    def __str__(self):
        return self.firma + ", " + self.name + " " + self.vorname


class Blogpost(models.Model):
    titel = models.CharField("Title", max_length=100)
    kurzbeschrieb = models.TextField("Kurzbeschrieb")
    datum = models.DateField("Publizierungsdatum")
    teaser_img = models.CharField("Vorschaubild", max_length=100)
    verfasser = models.ForeignKey("Stakeholder", on_delete=models.CASCADE)
    url = models.URLField("URL zum Post")

    class Meta:
        verbose_name_plural = "Blogposts"

    def __str__(self):
        return self.titel


class AngebotMessage(models.Model):
    name = models.CharField("Name", max_length=100)
    vorname = models.CharField("Vorname", max_length=100)
    email = models.EmailField("E-Mail")
    nachricht = models.TextField("Nachricht", blank=True)
    datum = models.DateField("Publizierungsdatum")
    angebot = models.ForeignKey("Angebot", on_delete=models.CASCADE)
    preisplan = models.ForeignKey("Preisplan", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Angebot Nachrichten"

    def __str__(self):
        return str(self.datum) + ": " + self.name + " " + self.vorname


class ContactMessage(models.Model):
    name = models.CharField("Name", max_length=100)
    vorname = models.CharField("Vorname", max_length=100)
    email = models.EmailField("E-Mail")
    nachricht = models.TextField("Nachricht", blank=True)
    datum = models.DateField("Publizierungsdatum")

    class Meta:
        verbose_name_plural = "Kontakt Nachrichten"

    def __str__(self):
        return str(self.datum) + ": " + self.name + " " + self.vorname
