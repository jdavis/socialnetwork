from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views import FriendsView

urlpatterns = patterns(
    '',
    url(r'^$', FriendsView.as_view(template_name='friends/index.html')),
)
