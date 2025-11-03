from django.shortcuts import render, get_object_or_404
from .models import Outfit, Occasion, Style

# Portada: 1 outfit por ocasión (el más reciente)
def index(request):
    occasions = Occasion.objects.all()
    featured = []
    for occ in occasions:
        o = occ.outfits.order_by("-created_at").first()
        if o:
            featured.append(o)
    return render(request, "showroom/index.html", {
        "featured_outfits": featured,
        "occasions": occasions
    })

# LISTAS
def outfit_list(request):
    outfits = Outfit.objects.select_related("occasion").prefetch_related("styles").all()
    return render(request, "showroom/outfit_list.html", {"outfits": outfits})

def occasion_list(request):
    occasions = Occasion.objects.all()
    return render(request, "showroom/occasion_list.html", {"occasions": occasions})

def style_list(request):
    styles = Style.objects.all()
    return render(request, "showroom/style_list.html", {"styles": styles})

# DETALLES
def outfit_detail(request, pk):
    outfit = get_object_or_404(
        Outfit.objects.select_related("occasion").prefetch_related("styles"),
        pk=pk
    )
    return render(request, "showroom/outfit_detail.html", {"outfit": outfit})

def occasion_detail(request, slug):
    occasion = get_object_or_404(Occasion, slug=slug)
    outfits = occasion.outfits.select_related("occasion").prefetch_related("styles")
    return render(request, "showroom/occasion_detail.html", {
        "occasion": occasion, "outfits": outfits
    })

def style_detail(request, slug):
    style = get_object_or_404(Style, slug=slug)
    outfits = style.outfits.select_related("occasion").prefetch_related("styles")
    return render(request, "showroom/style_detail.html", {
        "style": style, "outfits": outfits
    })
