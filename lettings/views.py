from django.shortcuts import render

from lettings.models import Letting


def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    letting_detail = Letting.objects.get(id=letting_id)
    context = {
        'title': letting_detail.title,
        'address': letting_detail.address,
    }
    return render(request, 'lettings/letting.html', context)
