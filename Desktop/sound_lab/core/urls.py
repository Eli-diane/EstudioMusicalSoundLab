import os
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# AQUI ESTÁ A CORREÇÃO 👇 (Adicionei o ", deletar_musica")
from estudio.views import index, deletar_musica 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('deletar/<int:musica_id>/', deletar_musica, name='deletar_musica'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/separated/', document_root=os.path.join(settings.BASE_DIR, 'separated'))