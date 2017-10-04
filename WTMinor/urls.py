from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='http://127.0.0.1:8000/login/')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    url(r'^content/', include('content.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^.*/$', RedirectView.as_view(url='http://127.0.0.1:8000/content/5'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
