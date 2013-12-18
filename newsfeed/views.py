from django.views import generic
from models import Status, LikesRelationship, StatusRelationship
from friends.models import Friendship

class IndexView(generic.TemplateView):
    template_name = 'newsfeed/index.html'
    context_object_name = 'latest_newsfeed'

    def get(self, request, *args, **kwargs):
        if "statusUpdate" in request.GET:
            status = Status(content=request.GET["statusUpdate"])
            status.save()
            relationship = StatusRelationship(user=request.user,
                                              status=status)
            relationship.save()
        
        # Get all friends.  This should be moved to a method elsewhere.
        friends = []
        for fr in Friendship.objects.all():
            if request.user == fr.user1:
                friends.append(fr.user2)
            if request.user == fr.user2:
                friends.append(fr.user1)
        friends.append(request.user)

        # Get statuses that friends have posted.
        s_relationships = []
        s = StatusRelationship.objects.order_by('-created')
        for r in s.all():
            if r.user in friends:
                if len(s_relationships) >= 25:
                    break
                else:
                    s_relationships.append(r)
        kwargs["statuses"] = s_relationships
        return super(IndexView, self).get(self, request, *args, **kwargs)
