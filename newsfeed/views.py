from django.views import generic
from models import Status, LikesRelationship, StatusRelationship
import friends.views

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
        
        friend_list = friends.views.get_friends(request.user)
        friend_list.append(request.user)
        # Get statuses that friends have posted.
        s_relationships = []
        s = StatusRelationship.objects.order_by('-created')
        for r in s.all():
            if r.user in friend_list:
                if len(s_relationships) >= 25:
                    break
                else:
                    s_relationships.append(r)
        kwargs["statuses"] = s_relationships
        return super(IndexView, self).get(self, request, *args, **kwargs)
