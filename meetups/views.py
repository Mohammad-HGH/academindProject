# * what should happen when certain url entered.


from django.shortcuts import render
from .models import Meetup


# from django.http import HttpResponse


# Create your views here.

def index(request):
    # ! tell to browser what send to user screen.
    # ! Django will call it when we're having incoming req for a certain url.
    # return HttpResponse('Hello World!!')

    # * Render get two params:
    # ? first param is request we got as argument in index(request)
    # ? second one is the name our template or path to our template (oath are relative from the template's folder)
    # ! without templates folder in the path

    # * extract all meetups in DB
    meetups = Meetup.objects.all()

    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup_title': selected_meetup.title,
            'meetup_description': selected_meetup.description
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })
