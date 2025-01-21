# Em clubeverde/views.py ou qualquer outro app
ffrom django.contrib import admin
from django.urls import path, include
from .views import home
from usuarios.views import usuario  # Importando a view do usuário
from loja.views import loja  # Importando a view da loja
from assinaturas.views import assinaturas  # Importando a view de assinaturas

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/assinaturas/', include('assinaturas.urls')),
    path('api/loja/', include('loja.urls')),

    # Novas URLs
    path('usuario/', usuario, name='usuario'),  # Página do usuário
    path('loja/', loja, name='loja'),  # Página da loja
    path('assinaturas/', assinaturas, name='assinaturas'),  # Página de assinaturas
]
