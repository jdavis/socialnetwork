from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import ModelForm, DateInput, DateField
from django.contrib.auth.models import User
from profiles.models import UserProfile


def profile(request, username=None):
    context = {}
    user = None

    if username is not None:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            context["error"] = "Can't find user %s." % username
    else:
        user = request.user

    context["userToView"] = user

    return render(request, 'profiles/index.html', context)

class EditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birthday', 'profile_picture', 'gender']

def edit(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        else:
            raise Exception("Failed.")

        return HttpResponseRedirect("/")
    else:
        form = EditForm(instance=profile)
        return render(request, 'profiles/edit.html', {'form': form})
