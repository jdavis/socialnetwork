from django.shortcuts import render, redirect
from django.views import generic

from models import Status, StatusForm, LikesRelationship, StatusRelationship

import friends.views


class IndexView(generic.TemplateView):
    template_name = 'newsfeed/index.html'
    context_object_name = 'latest_newsfeed'

    def get(self, request, *args, **kwargs):
        friend_list = friends.views.get_friends(request.user)
        friend_list.append(request.user)

        # Get statuses that friends have posted.
        statuses = Status.objects.order_by('-created')[:25]
        kwargs["statuses"] = statuses

        return super(IndexView, self).get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        s = Status()
        s.owner = request.user.get_profile()

        status = StatusForm(request.POST, instance=s)
        status.save()

        #relationship = StatusRelationship(user=request.user,
                                          #status=status)
        #relationship.save()

        return super(IndexView, self).get(self, request, *args, **kwargs)


