from django.shortcuts import render
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tweet
from .serializers import TweetSerializer
from rest_framework import status


class Tweets(APIView):
    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetSerializer(all_tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class TweetDetail(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound(detail="Tweet not found")

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk):
        tweet = self.get_object(pk)
        self.check_object_permissions(request, tweet)
        if tweet.user != request.user:
            raise PermissionDenied("Only the author can update")
        serializer = TweetSerializer(tweet, data=request.data, partial=True)
        if serializer.is_valid():
            tweet = serializer.save()
            serializer = TweetSerializer(tweet)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        self.check_object_permissions(request, tweet)
        if tweet.user != request.user:
            raise PermissionDenied("Only the author can delete")
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def get_all_tweets_for_view(request):
    try:
        tweets = Tweet.objects.all()
        return render(request, "tweets.html", {"tweets": tweets})
    except Tweet.DoesNotExist:
        return render(request, "not-found.html")
