from django.urls import path
from . import views

app_name = "showroom"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("outfits/", views.OutfitListView.as_view(), name="outfit_list"),
    path("outfits/<int:pk>/", views.OutfitDetailView.as_view(), name="outfit_detail"),
    path("occasions/", views.OccasionListView.as_view(), name="occasion_list"),
    path("occasions/<slug:slug>/", views.OccasionDetailView.as_view(), name="occasion_detail"),
    path("styles/", views.StyleListView.as_view(), name="style_list"),
    path("styles/<slug:slug>/", views.StyleDetailView.as_view(), name="style_detail"),
    path('enviar-idea/', views.EnviarOutfitIdeaView.as_view(), name='enviar_outfit_ideal'),
]