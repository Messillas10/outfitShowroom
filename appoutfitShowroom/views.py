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
    # Available filters via query params: ?style=<slug>&occasion=<slug>
    outfits = Outfit.objects.select_related("occasion").prefetch_related("styles").all()

    style_slug = request.GET.get("style")
    occasion_slug = request.GET.get("occasion")

    selected_style = None
    selected_occasion = None

    if style_slug:
        selected_style = Style.objects.filter(slug=style_slug).first()
        if selected_style:
            outfits = outfits.filter(styles=selected_style)

    if occasion_slug:
        selected_occasion = Occasion.objects.filter(slug=occasion_slug).first()
        if selected_occasion:
            outfits = outfits.filter(occasion=selected_occasion)

    # provide lists for filter UI
    styles = Style.objects.all()
    occasions = Occasion.objects.all()

    return render(request, "showroom/outfit_list.html", {
        "outfits": outfits,
        "styles": styles,
        "occasions": occasions,
        "selected_style": selected_style,
        "selected_occasion": selected_occasion,
    })

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
