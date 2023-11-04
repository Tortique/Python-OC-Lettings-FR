import sentry_sdk
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def trigger_error(request):
    try:
        return 1 / 0
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)
        return render(
            request, 'error.html', {'error_message': str(e)}, status=500)
