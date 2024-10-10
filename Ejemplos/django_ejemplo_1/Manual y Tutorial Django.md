DJANGO CONFIGURATION

Creaos Virtual environment
```bash
python -m venv myVenv
```

Ejecutamos el Venv en windows
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\myVenv\Scripts\activate
```

o Ejecutamos el Venv en Linux
```bash
source myVenv/Scripts/activate
```
Instalamos Django (individual)
```bash
pip install django
```

Instalamos Django, Flask, Requests (grupal)
```bash
pip install -r .\requirements
```

creamos proyecto django
```bash
django-admin startproject nombre_del_proyecto_django
```

Ingresamos al proyecto creado y creamos una app (en este ejemplo será el frontend)
```bash
cd nombre_del_proyecto_django
django-admin startapp nombre_de_app
```

Migrate manage
```bash
python manage.py migrate
```

[imagen](Ejemplos/django_ejemplo_1/imagenes_django/creacion_django.png)

Creamos usuario administrador (datos ejemplo, configurar prudentemente)
```bash
python manage.py createsuperuser 
> Email Address: admin@admin.com
> Password: admin
> Password (Again): admin
```
Ejecutar Servidor
```bash
python manage.py runserver
```
[imagen](Ejemplos/django_ejemplo_1/imagenes_django/Inicio_servidor.png)

[imagen](Ejemplos/django_ejemplo_1/imagenes_django/runserver.png)

[imagen](Ejemplos/django_ejemplo_1/imagenes_django/carpetas_1.png)

-------------------------------------------------------------------

Create Templates in app folder

Settings.py
```py
Installed_apps [
	Add app
	'nombre_de_app'
]
```

[imagen](Ejemplos/django_ejemplo_1/imagenes_django/config_app.png)


Configurar los templates de forma similar a:

Settings.py
```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

[imagen](Ejemplos/django_ejemplo_1/imagenes_django/config_templates_proyect.png)


urls.py (project)
agregar:
```py
	from django.urls import path, include
	path('', include("nombre_de_app.urls"))
```

[imagen](Ejemplos/django_ejemplo_1/imagenes_django/config_url_proyect.png)

Creamos el archivo urls.py en la app y copiamos el siguiente código:

urls.py (app)
```py
from . import views
from django.urls import path

urlpatterns = [
	path("", views.viewName, name="home"),
]
```

[imagen](Ejemplos/django_ejemplo_1/imagenes_django/config_url_app.png)


Views:
```py
from django.shortcuts import render

def viewName(request):
	context = {}
	return render(request, "nombre_de_app/home.html", context)
```

[imagen](Ejemplos/django_ejemplo_1/imagenes_django/config_app_views.png)

Configurar los views propios

--------------------------------------------------------------------
Al usar formularios configurar:

{% csrf_token %}
