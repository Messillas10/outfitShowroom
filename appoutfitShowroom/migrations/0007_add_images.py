"""Add image fields to Occasion and Style models.

Generated manually because `makemigrations` could not be executed in the current helper environment.
"""
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoutfitShowroom', '0006_remove_outfitidea_estilos_outfitidea_estilos'),
    ]

    operations = [
        migrations.AddField(
            model_name='occasion',
            name='image',
            field=models.ImageField(upload_to='occasions/', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='style',
            name='image',
            field=models.ImageField(upload_to='styles/', null=True, blank=True),
        ),
    ]
