# * what should happen when certain url entered.


from django.shortcuts import render


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

    meetups = [
        {
            'title': 'A first meetup',
            'location': 'Tehran',
            'slug': 'a-first-slug'
        },
        {
            'title': 'A second meetup',
            'location': 'NY',
            'slug': 'a-second-slug'
        },
    ]

    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title': 'meetup detail page',
        'description': 'This is the first meetup'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })
