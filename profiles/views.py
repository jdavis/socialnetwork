from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import ModelForm, DateInput, DateField
from django.contrib.auth.models import User
from profiles.models import UserProfile

class ProfileView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        user = None
        if "username" in request.GET:
            username = request.GET["username"]
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                kwargs["error"] = "Can't find user %s." % username
        else:
            user = request.user
        kwargs["userToView"] = user
        return super(ProfileView, self).get(self, request, *args, **kwargs)

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
