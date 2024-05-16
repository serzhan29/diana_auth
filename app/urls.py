from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from actors import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('actors.urls')),
    path('users/', include('users.urls', namespace="users")),
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Известные актеры"
