# * we should add url patterns variable
# ! Django looking with variable in that file.

from django.urls import path
from . import views

urlpatterns = [
    # ? path get 2 args:
    # * 1) Entered query after domain.
    # * 2) The view function which django should call if this query called by user.

    # ! WARNING: don't execute the views function. just point to it.
    path('meetups/', views.index, name='all-meetups'),  # ? our-domain.com/meetups/
    path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'),
]
