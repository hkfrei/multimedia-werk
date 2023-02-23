from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.urls import reverse
from django.core.mail import send_mail
from django.shortcuts import render
from datetime import datetime
from .models import Angebot, Blogpost, Referenz, Preisplan
from .forms import MessageForm
# Create your views here.


class HomeView(TemplateView):
    template_name = "kartenwerk/index.html"


class AngebotList(ListView):
    model = Angebot
    template_name = "kartenwerk/angebote.html"
    context_object_name = "angebote"


class AngebotDetail(DetailView):
    model = Angebot
    template_name = 'kartenwerk/angebot_detail.html'


class ReferenzenView(ListView):
    model = Referenz
    template_name = "kartenwerk/referenzen.html"
    context_object_name = "referenzen"


class AboutView(TemplateView):
    template_name = "kartenwerk/about.html"


class Blogposts(ListView):
    model = Blogpost
    template_name = "kartenwerk/blogposts.html"
    context_object_name = "blogposts"


class AngebotContact(CreateView):
    template_name = "kartenwerk/angebot_contact.html"
    form_class = MessageForm

    def get_success_url(self):
        return reverse("kartenwerk:success_message", kwargs={"preisplan_id": self.object.preisplan.id, "angebot_id": self.object.angebot.id, "message_id": self.object.id})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["angebot"] = Angebot.objects.get(pk=self.kwargs['angebot_id'])
        context["preisplan"] = Preisplan.objects.get(
            pk=self.kwargs['preisplan_id'])
        return context

    def form_valid(self, form):
        # we have to set some attributes which we do not get from the form
        self.object = form.save(commit=False)
        self.object.angebot = Angebot.objects.get(pk=self.kwargs['angebot_id'])
        self.object.preisplan = Preisplan.objects.get(
            pk=self.kwargs['preisplan_id'])
        self.object.datum = datetime.today()
        self.object.save()
        email_message = "Dies ist eine Nachricht von der Karten-Werk Website. \n \n" \
            + "Datum: " + str(self.object.datum.day) + "."\
            + str(self.object.datum.month) + "." \
            + str(self.object.datum.year) + "\n" \
            + "Produkt: " + self.object.angebot.name + "\n" \
            + "Preisplan: " + self.object.preisplan.name + "\n \n" \
            + "Name: " + str(form.cleaned_data.get("name")) + "\n"\
            + "Vorname: " + str(form.cleaned_data.get("vorname")) + "\n" \
            + "Email: " + form.cleaned_data.get("email") + "\n \n"\
            + "Nachricht: \n" \
            + form.cleaned_data.get("nachricht")
        try:
            send_mail(
                'Karten-Werk Website',
                email_message,
                'info@karten-werk.ch', ['hkfrei@karten-werk.ch',
                                        form.cleaned_data.get("email")],
                fail_silently=False
            )
        except:
            context = self.get_context_data()
            context["email_error"] = "Es gab einen Fehler beim E-Mail Versand. \n Bitte versuchen sie es nochmals oder treten sie telefonisch mit uns in Kontakt."
            return render(self.request, template_name=self.template_name, context=context)

        return super().form_valid(form)


class AngebotSuccessMessage(TemplateView):
    template_name = "kartenwerk/preisplan_success_message.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = Message.objects.get(pk=self.kwargs["message_id"])
        return context

    def get_success_url(self):
        message = Message.objects.get(pk=self.kwargs["message_id"])
        return reverse("kartenwerk:angebot_detail", kwargs={"pk": message.angebot.id})
