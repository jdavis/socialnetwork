from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns(
    '',
    url(r'^$', views.profile, name='profile_self'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),
)
