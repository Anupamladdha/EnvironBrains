from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def getUserProfile(request):
    return render(request, 'userProfile.html', {})

@login_required
def getUserData(request):
    context = {}
    return render(request, 'userData.html', context)