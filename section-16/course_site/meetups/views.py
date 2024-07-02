from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    meet = [
        {"title": "first meet up"},
        {"title": "second meet up"}
    ]
    return render(request, "meetups/index.html",{
        "meetus":meet
    })