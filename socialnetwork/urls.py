from django.conf import settings

from django.conf.urls import patterns, include, url

from django.conf.urls.static import static

urlpatterns = patterns(
    '',

    # App URLs
    url(r'^$', include('newsfeed.urls', namespace='newsfeed')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^friends/', include('friends.urls', namespace='friends')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
