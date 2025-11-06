from django.contrib import admin
from .models import Occasion, Style, Outfit, OutfitIdea

@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ("title", "occasion", "genero", "created_at")
    list_filter = ("occasion", "styles", "genero")
    search_fields = ("title", "description")
    
    
@admin.register(OutfitIdea)
class OutfitIdeaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "ocasion", "fecha_envio")
    list_filter = ("ocasion", "fecha_envio")
    search_fields = ("nombre", "email", "descripcion")
    date_hierarchy = "fecha_envio"
    filter_horizontal = ("estilos",)

