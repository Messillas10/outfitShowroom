from django import forms
from .models import OutfitIdea, Style
class OutfitIdeaForm(forms.ModelForm):
    estilos = forms.ModelMultipleChoiceField(
        queryset=Style.objects.all().order_by('name'),  # o .order_by('nombre')
        widget=forms.SelectMultiple,                    # desplegable múltiple nativo
        required=False,
        label='Estilos'
    )

    class Meta:
        model = OutfitIdea
        fields = ['nombre', 'email', 'descripcion', 'ocasion', 'estilos', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe tu outfit ideal...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'tu@email.com'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
        }
