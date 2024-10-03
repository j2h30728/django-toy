from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_tweets),
    path("<int:tweet_id>", views.get_tweet_detail),
]
