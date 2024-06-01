from .models import Feed
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def index(request):
    #data = Feed.objects.all()
    #return HttpResponse(data)

def index(request):
    press = Feed.objects.all()
    context = {
        "news": press
    }
    return render(request, "press/home.html", context)