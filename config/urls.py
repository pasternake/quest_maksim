from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("anketa/", include("anketa.urls")),
    path("", RedirectView.as_view(url="/anketa/", permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
