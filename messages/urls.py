from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from messages import views

urlpatterns = patterns(
    '',
    url(r'^$', views.messages, name='messages'),
    url(r'^(?P<user_id>\d+)/$', views.messages, name='messages'),
    url(r'^new/(?P<user_id>\d+)/$', views.new_message, name='messages')
)
