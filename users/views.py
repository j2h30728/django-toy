from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from tweets.serializers import TweetSerializer


@api_view(["GET"])
def get_all_users(request):
    all_users = User.objects.all()
    serializer = UserSerializer(all_users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_user_detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise NotFound(detail="User not found")

    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
def get_all_tweets_written_by_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        all_tweets_written_by_user = user.tweets.all()
    except User.DoesNotExist:
        raise NotFound(detail="User not found")

    serializer = TweetSerializer(all_tweets_written_by_user, many=True)
    return Response(serializer.data)
