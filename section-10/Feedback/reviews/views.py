from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import reviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review

# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = reviewForm()
        return render(request, "reviews/review.html", {
        "form": form,
        })
        
    def post(self, request):
        form = reviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")    
        
        return render(request, "reviews/review.html", {
            "form": form,
        })
            
            
# def review(request):
#     if request.method == "POST":
#         form = reviewForm(request.POST)
##########2
#         if form.is_valid():
#             form.save()
##########1
#             # data = form.cleaned_data
#             # review = Review(
#             #     user_name = data['user_name'],
#             #     Review_text = data['review_text'],
#             #     rating= data['rating'],
#             # )
#             # review.save()
#             return HttpResponseRedirect("/thank-you")
#     else:    
#         form = reviewForm()
        
#     return render(request, "reviews/review.html", {
#         "form": form,
#     })
    
###########3        to insert update a new data with the new data
# def review(request):
#     if request.method == "POST":
#         existing_data = Review.objects.get(pk=1)
#         form = reviewForm(request.POST, instance=existing_data)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#     else:    
#         form = reviewForm()
        
#     return render(request, "reviews/review.html", {
#         "form": form,
#     })

##############################################################################################################
#####1
# def thank_you(request):
#     return render(request, "reviews/thank_you.html")

#####2
# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html")

#####3
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works"
        return context
    
    
class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context
        