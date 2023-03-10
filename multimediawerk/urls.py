from django.urls import path
from . import views

app_name = 'multimediawerk'
urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("angebote", views.AngebotList.as_view(), name="angebot"),
    path("angebot/<int:pk>", views.AngebotDetail.as_view(), name="angebot_detail"),
    path("referenzen", views.ReferenzenView.as_view(), name="referenzen"),
    path("ueber-uns", views.AboutView.as_view(), name="about"),
    path("blog", views.Blogposts.as_view(), name="blog"),
    path("angebot/<int:angebot_id>/preisplan/<int:preisplan_id>/contact",
         views.AngebotContact.as_view(), name="angebot_message"),
    path("angebot/<int:angebot_id>/preisplan/<int:preisplan_id>/message/<int:message_id>",
         views.AngebotSuccessMessage.as_view(), name="angebot_success_message"),
    path("kontakt", views.Contact.as_view(), name="contact_message"),
    path("kontakt/message/<int:message_id>",
         views.ContactSuccessMessage.as_view(), name="contact_success_message")
]
