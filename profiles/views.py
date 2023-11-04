from django.shortcuts import render

from profiles.models import Profile


def index(request):
    """
    View function to display a list of user profiles.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML page displaying a list of user profiles.

    Queries the database for all user profiles, and then renders the 'profiles/index.html' template
    with the list of profiles provided in the 'profiles_list' context variable.

    Example Usage:
        To display a list of user profiles,
         you can include this view in your Django project's URLs configuration.

    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    View function to display a user's profile detail.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is being viewed.

    Returns:
        HttpResponse: A rendered HTML page displaying the user's profile.

    Retrieves the user's profile from the database using the provided username,
     and then renders the
    'profiles/profile.html' template with the user's profile information
    provided in the 'profile' context variable.

    Example Usage:
        To display a user's profile, you can include this view
        in your Django project's URLs configuration, passing the
        username as a parameter in the URL.
    """
    profile_detail = Profile.objects.get(user__username=username)
    context = {'profile': profile_detail}
    return render(request, 'profiles/profile.html', context)
