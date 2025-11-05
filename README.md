# Outfit Showroom

Proyecto Django simple para mostrar "outfits" categorizados por ocasiones y estilos.

Requisitos
- Python 3.8+ (o la que uses en el virtualenv)
- virtualenv activado (se detectó `.venv` en el workspace)

Instrucciones rápidas (PowerShell / Windows)

1. Activar virtualenv (si existe):

```powershell
C:/Users/"usuario"/Projects/outfitShowroom/outfitShowroom/.venv/Scripts/Activate.ps1
```

2. Instalar dependencias (si `requirements.txt` existe), o instalar Django si es necesario:

```powershell
C:/Users/"usuario"/Projects/outfitShowroom/outfitShowroom/.venv/Scripts/python.exe -m pip install -r requirements.txt
# o
C:/Users/"usuario"/Projects/outfitShowroom/outfitShowroom/.venv/Scripts/python.exe -m pip install Django
```

3. Aplicar migraciones:

```powershell
C:/Users/"usuario"/Projects/outfitShowroom/outfitShowroom/.venv/Scripts/python.exe manage.py migrate
```

4. Cargar datos de ejemplo (opcional):

```powershell
C:/Users/"usuario"/Projects/outfitShowroom/outfitShowroom/.venv/Scripts/python.exe manage.py loaddata fixtures/initial_data.json
```

5. Ejecutar servidor de desarrollo:

```powershell
C:/Users/"usuario"/Projects/outfitShowroom/outfitShowroom/.venv/Scripts/python.exe manage.py runserver
```

6. Abrir en el navegador:

http://127.0.0.1:8000/

Tests

Para ejecutar tests:

```powershell
C:/Users/"usuario"/Projects/outfitShowroom/outfitShowroom/.venv/Scripts/python.exe manage.py test
```

Notas
- Ya hay plantillas en `appoutfitShowroom/templates/showroom` y estilos en `static/css/estilos.css`.

Siguientes pasos sugeridos
- Añadir paginación y filtros en listas.
- Implementar búsqueda (backend y frontend).
- Mejorar la gestión de imágenes (subida, thumbnails).
- Agregar autenticación y panel de administración para usuarios no técnicos.
