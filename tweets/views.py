from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tweet
from .serializers import TweetSerializer


class Tweets(APIView):
    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data)


class TweetDetail(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound(detail="Tweet not found")

    def get(self, request, pk):
        serializer = TweetSerializer(self.get_object(pk))
        return Response(serializer.data)


def get_all_tweets_for_view(request):
    try:
        tweets = Tweet.objects.all()
        return render(request, "tweets.html", {"tweets": tweets})
    except Tweet.DoesNotExist:
        return render(request, "not-found.html")
