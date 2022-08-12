# * what should happen when certain url entered.


from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # tell to browser what send to user screen.
    # Django will call it when we're having incoming req for a certain url.
    return HttpResponse('Hello World!!')
