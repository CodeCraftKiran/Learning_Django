from django.urls import path
from . import views

urlpatterns = [
    # path("", views.review),
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewListView.as_view()),
    # path("reviews/<int:id>", views.SingleReviewView.as_view())
    path("reviews/<int:pk>", views.SingleReviewView.as_view())  # pk=Primary Key
]
