from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from messages import views

urlpatterns = patterns(
    '',
    url(r'^$', views.messages, name='messages')
)
