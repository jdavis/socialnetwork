from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello world. \"Drop the 'the'\""
                        "-- Justin Timberlake")
