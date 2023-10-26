from django.shortcuts import render

from profiles.models import Profile


def index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    profile_detail = Profile.objects.get(user__username=username)
    context = {'profile': profile_detail}
    return render(request, 'profiles/profile.html', context)
