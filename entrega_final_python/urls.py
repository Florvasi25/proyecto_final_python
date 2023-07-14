from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('inicio.urls')),
    path('usuario/', include('usuario.urls')),
    path('mensajeria/', include('mensajeria.urls')),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)