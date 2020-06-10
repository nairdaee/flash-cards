from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    current_user=request.user.id
    profile_image=Profile.objects.filter(id=current_user)
    profile=profile_image.reverse()[0:1]
    users=User.objects.all().exclude(id=request.user.id)
    return render(request, 'home.html', {"profile":profile,"users":users})
