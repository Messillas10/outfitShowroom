from django.urls import path
from . import views

app_name = "showroom"

urlpatterns = [
    path("", views.index, name="index"),
    path("outfits/", views.outfit_list, name="outfit_list"),
    path("outfits/<int:pk>/", views.outfit_detail, name="outfit_detail"),
    path("occasions/", views.occasion_list, name="occasion_list"),
    path("occasions/<slug:slug>/", views.occasion_detail, name="occasion_detail"),
    path("styles/", views.style_list, name="style_list"),
    path("styles/<slug:slug>/", views.style_detail, name="style_detail"),
    path('enviar-idea/', views.enviar_outfit_ideal, name='enviar_outfit_ideal'),
]