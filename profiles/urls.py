from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns(
    '',
    url(r'^$', views.profiles, name='profiles'),
    url(r'^edit/', views.edit, name='edit'),
)
