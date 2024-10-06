from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from tweets.serializers import TweetSerializer


class Users(APIView):
    def get(self, request):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        serializer = UserSerializer(self.get_object(pk))
        return Response(serializer.data)


class TweetsWrittenByUser(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            all_tweets_written_by_user = user.tweets.all()
        except User.DoesNotExist:
            raise NotFound(detail="User not found")

        serializer = TweetSerializer(all_tweets_written_by_user, many=True)
        return Response(serializer.data)
