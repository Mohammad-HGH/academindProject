# * what should happen when certain url entered.


from django.shortcuts import render, redirect
from .models import Meetup, Participant
from .forms import RegistrationForm


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

        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                # ! if incoming email is valid in DB, don't save & show existing one.
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)

                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })
