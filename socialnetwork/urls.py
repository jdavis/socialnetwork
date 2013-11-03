from django.conf import settings

from django.conf.urls import patterns, include, url

from django.conf.urls.static import static


    url(r'^$', include('newsfeed.urls', namespace='newsfeed')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
