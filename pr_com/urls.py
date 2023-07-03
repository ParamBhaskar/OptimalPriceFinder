from django.conf import settings
# from django.conf.urls import url, static
# from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # url(r'^api/crawl/', views.crawl, name='crawl'),
    path('', views.crawl2, name='crawl2'),
    
]

# This is required for static files while in development mode. (DEBUG=TRUE)
# No, not relevant to scrapy or crawling :)
# if settings.DEBUG:
#     urlpatterns += static.static(settings.STATIC_URL,
#                                  document_root=settings.STATIC_ROOT)
#     urlpatterns += static.static(settings.MEDIA_URL,
#                                  document_root=settings.MEDIA_ROOT)
