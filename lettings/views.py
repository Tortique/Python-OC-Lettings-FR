from django.shortcuts import render

from lettings.models import Letting


def index(request):
    """
    View function to display a list of letting properties.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML page displaying a list of letting properties.

    Queries the database for all letting properties using the Letting model,
    and then renders the 'lettings/index.html'
    template with the list of letting properties provided in the 'lettings_list' context variable.

    Example Usage:
        To display a list of letting properties, you can include this view
        in your Django project's URLs configuration.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View function to display details of a letting property.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The unique identifier of the letting property be viewed.

    Returns:
        HttpResponse: A rendered HTML page displaying the details
        of the specified letting property.

    Retrieves the letting property from the database using the provided letting_id,
    and then renders the
    'lettings/letting.html' template with the letting property's title
    and address information provided in the
    'title' and 'address' context variables.

    Example Usage: To display details of a specific letting property,
    you can include this view in your Django
    project's URLs configuration, passing the letting_id as a parameter in the URL.
    """
    letting_detail = Letting.objects.get(id=letting_id)
    context = {
        'title': letting_detail.title,
        'address': letting_detail.address,
    }
    return render(request, 'lettings/letting.html', context)


def server_error_500(request):
    """
    View function to handle and display a 500 Internal Server Error.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML error page indicating a 500 Internal Server Error.

    Renders the 'error.html' template with the 'error_code' context variable set to 500,
    indicating an internal
    server error. The response status code is also set to 500.

    Example Usage: This view can be used to handle
    and display custom error pages for internal server errors (500) in
    your Django project.
    """
    return render(request, 'error.html', {'error_code': 500}, status=500)


def custom_404(request):
    """
    View function to handle and display a custom 404 Not Found Error.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML error page indicating a 404 Not Found Error.

    Renders the 'error.html' template with the 'error_code' context variable set to 404,
    indicating a "Not Found" error.
    The response status code is also set to 404.

    Example Usage: This view can be used to handle
    and display custom error pages for "Not Found" errors (404) in
    your Django project.
    """
    return render(request, 'error.html', {'error_code': 404}, status=404)
