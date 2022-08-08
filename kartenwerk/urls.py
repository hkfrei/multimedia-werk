from django.urls import path
from . import views

app_name = 'kartenwerk'
urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("angebote", views.AngebotList.as_view(), name="angebot"),
    path("angebot/<int:pk>", views.AngebotDetail.as_view(), name="angebot_detail"),
    path("referenzen", views.ReferenzenView.as_view(), name="referenzen"),
    path("ueber-uns", views.AboutView.as_view(), name="about")
]
