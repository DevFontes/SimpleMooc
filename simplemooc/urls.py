from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

#app_name='core'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cursos/', include('simplemooc.courses.urls', namespace='courses')),
    url(r'^', include('simplemooc.core.urls', namespace='core')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)