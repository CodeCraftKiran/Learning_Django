from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december":None,
}


# Create your views here.
def index(request):
    months = monthly_challengs.keys()
    return render(request, "challenges/index.html", {
        'months': months,
    })



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
        return render(request, "challenges/challenges.html", {
            "text": challenge,
            "month": month
        })
    
        # response_html = render_to_string("challenges/challenges.html")
        # return HttpResponse(response_html)
    except:
        # return HttpResponseNotFound("<h1>Please check the spelling.</h1>")
        
        # response = render_to_string("404.html")
        # return HttpResponseNotFound(response)
        
        raise Http404()    # HERE IT FIND A FILE WITH NAME 404.HTML AND RAISE A EXCEPTION