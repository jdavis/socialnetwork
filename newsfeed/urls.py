from django.conf.urls import patterns, url

from newsfeed import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(template_name='newsfeed/index.html')),
    url(r'^like/(?P<status_id>\d+)/$', views.like_status, name='like_status')
)
