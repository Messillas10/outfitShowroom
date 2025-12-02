from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib import messages

from .models import Outfit, Occasion, Style, OutfitIdea
from .forms import OutfitIdeaForm


class IndexView(TemplateView):
    """Portada: muestra una selección (1 outfit por ocasión, el más reciente)."""
    template_name = 'showroom/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        occasions = Occasion.objects.all()
        featured = []
        for occ in occasions:
            o = occ.outfits.order_by("-created_at").first()
            if o:
                featured.append(o)
        context.update({
            'featured_outfits': featured,
            'occasions': occasions,
        })
        return context


class OutfitListView(ListView):
    """Listado de outfits con filtros por style, occasion y genero."""
    model = Outfit
    template_name = 'showroom/outfit_list.html'
    context_object_name = 'outfits'

    def get_queryset(self):
        qs = Outfit.objects.select_related('occasion').prefetch_related('styles').all()

        style_slug = self.request.GET.get('style')
        occasion_slug = self.request.GET.get('occasion')
        genero = self.request.GET.get('genero')

        # keep selected choices on the view instance so get_context_data can read them
        self.selected_style = None
        self.selected_occasion = None
        self.selected_genero = None

        if style_slug:
            self.selected_style = Style.objects.filter(slug=style_slug).first()
            if self.selected_style:
                qs = qs.filter(styles=self.selected_style)

        if occasion_slug:
            self.selected_occasion = Occasion.objects.filter(slug=occasion_slug).first()
            if self.selected_occasion:
                qs = qs.filter(occasion=self.selected_occasion)

        if genero:
            valid_generos = [g[0] for g in Outfit.GENERO_CHOICES]
            if genero in valid_generos:
                self.selected_genero = genero
                qs = qs.filter(genero=self.selected_genero)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'styles': Style.objects.all(),
            'occasions': Occasion.objects.all(),
            'generos': Outfit.GENERO_CHOICES,
            'selected_style': getattr(self, 'selected_style', None),
            'selected_occasion': getattr(self, 'selected_occasion', None),
            'selected_genero': getattr(self, 'selected_genero', None),
        })
        return context


class OccasionListView(ListView):
    model = Occasion
    template_name = 'showroom/occasion_list.html'
    context_object_name = 'occasions'


class StyleListView(ListView):
    model = Style
    template_name = 'showroom/style_list.html'
    context_object_name = 'styles'


class OutfitDetailView(DetailView):
    model = Outfit
    template_name = 'showroom/outfit_detail.html'
    context_object_name = 'outfit'


class OccasionDetailView(DetailView):
    model = Occasion
    template_name = 'showroom/occasion_detail.html'
    context_object_name = 'occasion'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfits'] = self.object.outfits.select_related('occasion').prefetch_related('styles')
        return context


class StyleDetailView(DetailView):
    model = Style
    template_name = 'showroom/style_detail.html'
    context_object_name = 'style'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfits'] = self.object.outfits.select_related('occasion').prefetch_related('styles')
        return context


class EnviarOutfitIdeaView(CreateView):
    model = OutfitIdea
    form_class = OutfitIdeaForm
    template_name = 'showroom/enviar_outfit_ideal.html'

    def form_valid(self, form):
        # let CreateView save the object
        response = super().form_valid(form)
        messages.success(self.request, '¡Gracias! Hemos recibido tu idea de outfit.')
        return response

    def get_success_url(self):
        # redirect back to the form with a query param to indicate success
        return reverse('showroom:enviar_outfit_ideal') + '?ok=1'

