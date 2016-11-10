from django.shortcuts import render

# Create your views here.
from user_manager.models import Member
from user_profile.models import Media


def profile(request,username):
    current_user = Member.objects.get(username=username)
    photos = Media.objects.filter(user_id=current_user).order_by("-created")
    return render(request, 'user_profile/profile.html', {
        'username': username,
        'user': current_user,
        'post': photos
    })

def followers(request,username):
    pass

def following(request,username):
    pass