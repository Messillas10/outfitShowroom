from django.contrib import admin
from .models import Occasion, Style, Outfit

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

