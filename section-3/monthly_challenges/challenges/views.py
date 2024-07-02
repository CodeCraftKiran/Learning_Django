from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challengs = {
    "january":"One month without alcohol and soda.",
    "february":"One month of being total Vegan.",
    "march":"One month of sugar detox.",
    "april":"One month of running 1 mile each day.",
    "may":"One month of yoga every day.",
    "june":"One month of social media detox.",
    "july":"One month of caffeine detox.",
    "august":"One month of eating only at home or home-cooked meal.",
    "september":"One month without alcohol and soda.",
    "october":"One month of being total Vegan.",
    "november":"One month of sugar detox.",
    "december":"One month of running 1 mile each day.",
}


# Create your views here.
def index(request):
    list_item = ""
    months = monthly_challengs.keys()
    for month in months:
        capitalize_month = month.capitalize()
        month_path = reverse("name_of_month", args=[month])
        list_item += f"<li><a href={month_path}>{capitalize_month}</a></li>"

    response_data = f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)


def challenge_month_by_number(request, month):
    all_month = list(monthly_challengs.keys())
    if month > len(all_month):
        return HttpResponseNotFound("There are only 12 months in a year")
    redirect_month = all_month[month-1]
    redirect_path = reverse("name_of_month", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def challenge_month(request, month):
    try:
        challenge = monthly_challengs[month]
        response_html = f"<h1>{challenge}</h1>"
        return HttpResponse(response_html)
    except:
        return HttpResponseNotFound("<h1>Please check the spelling.</h1>")