from django.conf import settings
from django.contrib.gis import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^', include('apps.index.urls')),
    url(r'^index/', include('apps.index.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^maps/', include('apps.maps.urls', namespace='maps'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
