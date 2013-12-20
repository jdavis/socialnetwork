from django.conf.urls import patterns, url

from profiles import views
from views import ProfileView

urlpatterns = patterns(
    '',
    url(r'^$', ProfileView.as_view(template_name='profiles/index.html')),
    url(r'^edit/', views.edit, name='edit'),
)
