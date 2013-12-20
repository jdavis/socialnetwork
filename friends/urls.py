from django.conf.urls import patterns, url

from friends import views

urlpatterns = patterns(
    '',
    url(r'^$', views.show_friends, name='show_friends'),
)
