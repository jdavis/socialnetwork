from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User
from models import Friendship

class FriendsView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        friend_list = get_friends(request.user)
        kwargs["friends"] = friend_list
        return super(FriendsView, self).get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        friend_list = get_friends(request.user)
        kwargs["friends"] = friend_list

        # Determine if user exists.
        friend_name = request.POST["friend_name"]
        friend = None
        try:
            friend = User.objects.get(username=friend_name)
        except User.DoesNotExist:
            kwargs["error"] = "Couldn't find user %s" % friend_name

        if friend:
            # Determine if user is already a friend.
            isAlreadyFriend = False
            for friend in friend_list:
                if friend_name == friend.username:
                    isAlreadyFriend = True

            if not isAlreadyFriend:
                f = Friendship(user1=request.user, user2=friend)
                f.save()
                friend_list.append(friend)
            else:
                msg = "You're already friends with %s." % friend_name
                kwargs["error"] = msg

        return super(FriendsView, self).get(self, request, *args, **kwargs)



def get_friends(user):
    friends = []
    for fr in Friendship.objects.all():
        if user == fr.user1:
            friends.append(fr.user2)
        if user == fr.user2:
            friends.append(fr.user1)
    return friends
