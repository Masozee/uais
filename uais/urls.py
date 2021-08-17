
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

admin.sites.AdminSite.site_header = 'University Centre of Excellence – AIDS Research Center International Symposium 2021'
admin.sites.AdminSite.site_title = 'University Centre of Excellence – AIDS Research Center International Symposium 2021'
admin.sites.AdminSite.index_title = 'University Centre of Excellence – AIDS Research Center International Symposium 2021'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.url')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)