from django.views import generic


class IndexView(generic.ListView):
    template_name = 'newsfeed/index.html'
    context_object_name = 'latest_newsfeed'
