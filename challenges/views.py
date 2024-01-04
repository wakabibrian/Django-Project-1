from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Work for atleast 20 minutes everyday!",
    "march": "Learn Django for atleast 20 minutes everyday!",
    "april": "Eat no meat for the entire month",
    "may": "Work for atleast 20 minutes everyday!",
    "june": "Learn Django for atleast 20 minutes everyday!",
    "july": "Eat no meat for the entire month",
    "august": "Work for atleast 20 minutes everyday!",
    "september": "Learn Django for atleast 20 minutes everyday!",
    "october": "Eat no meat for the entire month",
    "november": "Work for atleast 20 minutes everyday!",
    "december": "Learn Django for atleast 20 minutes everyday!"
}


def index(request):

    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        captalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{captalized_month}<a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenges/redirect_month
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
