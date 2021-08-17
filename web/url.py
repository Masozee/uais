from django.urls import path, include, re_path
from django.views.generic import TemplateView

from web import views as webviews


urlpatterns = [
    path('', webviews.Home, name='home'),
    path('speakers/', webviews.Speakers, name='speakers'),
    path('jadwal/', webviews.event, name='schedule'),
    path('sponsors/', TemplateView.as_view(template_name='web/sponsors.html'), name='sponsors'),
    path('teams/',webviews.Teams , name='teams'),
    path('contact/', TemplateView.as_view(template_name='web/contact.html'), name='contact'),
    path('about/', TemplateView.as_view(template_name='web/about.html'), name='about'),
    path('gallery/', TemplateView.as_view(template_name='web/gallery.html'), name='gallery'),
    path('blog/', TemplateView.as_view(template_name='web/blog.html'), name='blog'),
    path('blog/detail/', TemplateView.as_view(template_name='web/blog-single.html'), name='blog-detail'),
    re_path('blog/(?P<artikel_slug>[\w-]+)/$', webviews.TulisanDetail, name='tulisan-detail'),
]