from django.urls import path

from . import views

urlpatterns = [
    path("<int:month>", views.challenge_month_by_number),
    path("<str:month>", views.challenge_month),
]