# Outfit Showroom

Proyecto Django simple para mostrar "outfits" categorizados por ocasiones y estilos.

## Resumen

Este repositorio contiene una aplicación Django pequeña llamada `appoutfitShowroom` que incluye modelos, vistas y plantillas para listar y detallar outfits, estilos y ocasiones. La base de datos por defecto es SQLite (`db.sqlite3`) y hay imágenes y datos de ejemplo incluidos en `media/` y `fixtures/initial_data.json`.

## Requisitos

- Python 3.8 o superior (recomendado: 3.8+)
- virtualenv/venv (se detectó `.venv` en el workspace durante el desarrollo)
- Dependencias listadas en `requirements.txt`:
	- Django>=3.2,<5.0
	- Pillow>=9.0.0

## Instalación y ejecución

Sigue estos pasos desde la raíz del repositorio (`c:\Users\...\Projects\outfitShowroom`). Reemplaza las rutas si tu virtualenv está en otro sitio.

1) (Opcional) Crear y activar un virtualenv si no tienes uno:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Si ya tienes un virtualenv, actívalo (ejemplo):

```powershell
C:\path\to\your\.venv\Scripts\Activate.ps1
```

3) Instalar dependencias:

```powershell
python -m pip install -r requirements.txt
```

4) Aplicar migraciones:

```powershell
python manage.py migrate
```

5) (Opcional) Cargar datos de ejemplo:

```powershell
python manage.py loaddata fixtures/initial_data.json
```

6) (Opcional) Crear un superusuario para acceder al admin:

```powershell
python manage.py createsuperuser
```

7) (Opcional en desarrollo) Recopilar archivos estáticos si los necesitas:

```powershell
python manage.py collectstatic --noinput
```

8) Ejecutar servidor de desarrollo:

```powershell
python manage.py runserver
```

Luego abre en tu navegador: http://127.0.0.1:8000/

## Ejecutar tests

```powershell
python manage.py test
```

## Estructura importante del proyecto

- `appoutfitShowroom/` — aplicación Django principal (modelos, vistas, templates).
- `outfitShowroom/` — configuración del proyecto (settings, urls, wsgi/asgi).
- `media/` — archivos subidos (imágenes de estilos/outfits/occasions).
- `static/` — assets estáticos (CSS).
- `fixtures/initial_data.json` — datos de ejemplo cargables con `loaddata`.

## Notas y troubleshooting

- Si Pillow falla en Windows al instalar, instala las dependencias de compilación de Microsoft (Visual C++ Build Tools) o usa una rueda precompilada.
- Si ves errores de permisos al escribir en `media/` o `db.sqlite3`, revisa permisos de la carpeta.
- Para servir archivos media en producción, configura un servidor (nginx, S3, etc.). Django sólo sirve media automáticamente cuando `DEBUG=True`.

## Siguientes mejoras sugeridas

- Añadir paginación y filtros en las vistas de lista.
- Implementar búsqueda (backend + frontend).
- Mejorar la gestión de imágenes (subida segura, thumbnails procesados, almacenamiento externo).
- Añadir autenticación/roles y panel de administración para usuarios no técnicos.

## Contribuir

Si quieres contribuir:

1. Haz fork del repositorio y crea una rama con un nombre claro (`feature/mi-cambio`).
2. Añade tests cuando sea posible.
3. Abre un PR describiendo los cambios.

## Licencia

Incluye aquí la licencia del proyecto (si aplica). Si no hay una, considera añadir un archivo `LICENSE`.

## Contacto

Si tienes dudas o quieres que haga ajustes al README, dímelo y lo actualizo.
