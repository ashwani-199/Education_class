from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from tution_management.common_modules.mainservices import MainService
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap

sitemaps = {
    'static': StaticSitemap
}

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views'),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('', include('apps.contact.urls')),
    
]

handler404 = MainService.error_404
handler500 = MainService.error_500
handler403 = MainService.error_403
handler400 = MainService.error_400



if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

if settings.DEBUG == False:
    urlpatterns += staticfiles_urlpatterns()