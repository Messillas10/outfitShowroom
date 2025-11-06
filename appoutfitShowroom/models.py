from django.db import models

class Occasion(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Outfit(models.Model):
    title = models.CharField(max_length=100)
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE, related_name="outfits")
    styles = models.ManyToManyField(Style, related_name="outfits")
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='outfits/', blank=True, null=True)
    GENERO_MUJER = 'mujer'
    GENERO_HOMBRE = 'hombre'
    GENERO_AMBIGUO = 'ambiguo'
    GENERO_CHOICES = (
        (GENERO_MUJER, 'Mujer'),
        (GENERO_HOMBRE, 'Hombre'),
        (GENERO_AMBIGUO, 'Ambiguo'),
    )
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, default=GENERO_AMBIGUO)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "title"]

    def __str__(self):
        return self.title
    
    
class OutfitIdea(models.Model):
    OCASIONES = [
        ('Casual', 'Casual'),
        ('Formal', 'Formal'),
        ('Playa', 'Día de playa'),
        ('Trabajo', 'Trabajo'),
        ('Noche', 'De noche'),
    ]

    ESTILOS = [
        ('Minimalista', 'Minimalista'),
        ('Sporty', 'Sporty'),
        ('Urban-Chic', 'Urban-Chic'),
        ('Vintage', 'Vintage'),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    descripcion = models.TextField()
    ocasion = models.CharField(max_length=20, choices=OCASIONES)
    estilos = models.ManyToManyField('Style', blank=True)
    imagen = models.ImageField(upload_to='outfit_ideas/', blank=True, null=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.ocasion}"

