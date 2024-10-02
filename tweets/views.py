from django.shortcuts import render
from .models import Tweet


def get_all_tweets(request):
    try:
        tweets = Tweet.objects.all()
        return render(request, "tweets.html", {"tweets": tweets})
    except Tweet.DoesNotExist:
        return render(request, "not-found.html")


def get_tweet_detail(request, tweet_pk):
    try:
        tweet = Tweet.objects.get(pk=tweet_pk)
        return render(request, "tweet_detail.html", {"tweet": tweet})
    except Tweet.DoesNotExist:
        return render(request, "not-found.html")
