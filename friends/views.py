# Create your views here.
from models import Friendship

def get_friends(user):
    friends = []
    for fr in Friendship.objects.all():
        if user == fr.user1:
            friends.append(fr.user2)
        if user == fr.user2:
            friends.append(fr.user1)
    return friends
