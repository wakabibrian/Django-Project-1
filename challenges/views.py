from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def monthly_challenge(request, month):
    challenge_text = None

    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Work for atleast 20 minutes everyday!"
    elif month == "march":
        challenge_text = "Learn Django for atleast 20 minutes everyday!"
    else:
        return HttpResponseNotFound("This Month is not supported")
    return HttpResponse(challenge_text)
