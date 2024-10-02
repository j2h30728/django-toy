from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_tweets),
    path("tweets/<int:tweet_pk>", views.get_tweet_detail),
]
