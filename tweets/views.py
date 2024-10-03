from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer


@api_view(["GET"])
def get_all_tweets(request):
    all_tweets = Tweet.objects.all()
    serializer = TweetSerializer(all_tweets, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_tweet_detail(request, tweet_id):
    try:
        tweet = Tweet.objects.get(pk=tweet_id)
    except Tweet.DoesNotExist:
        raise NotFound(detail="Tweet not found")

    serializer = TweetSerializer(tweet)
    return Response(serializer.data)


def get_all_tweets_for_view(request):
    try:
        tweets = Tweet.objects.all()
        return render(request, "tweets.html", {"tweets": tweets})
    except Tweet.DoesNotExist:
        return render(request, "not-found.html")
