from django.shortcuts import render

def profiles(request):
    # NOTE:  Why is there a list of profiles?
    profile = request.user.userprofile_set.all()[0]
    return render(request, 'profiles/index.html', {"profile": profile})
