from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    meetups = [
        {
            "title": "A First meetup",
            "location": "New York",
            "slug": "a-first-meetup",
        },
        {
            "title": "A Second meetup",
            "location": "Pari",
            "slug": "a-second-meetup",
        },
    ]    
    return render(request, "meetups/index.html",{
        "show_meetups":True,
        "meetups": meetups
    })