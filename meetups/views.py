from django.shortcuts import render, redirect

from meetups.forms import RegistrationForm
from meetups.models import Meetup, Participant


# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html',
                  {"meetups": meetups,
                   "show_meetups": True}
                  )


def meetup_detail(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == "GET":
            registration_form = RegistrationForm()

        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup-details.html', {
            "meetup_found": True,
            "meetup": selected_meetup,
            "form": registration_form
        })
    except Exception as e:
        print(e)
        return render(request, 'meetups/meetup-details.html', {
            "meetup_found": False})


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, "meetups/registration-success.html",{
        "meetup": meetup
    })
