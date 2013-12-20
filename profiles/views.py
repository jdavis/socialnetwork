from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import ModelForm, DateInput, DateField
from profiles.models import UserProfile

def profiles(request):
    profile = request.user.userprofile
    return render(request, 'profiles/index.html', {"profile": profile})

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
