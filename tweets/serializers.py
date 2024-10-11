from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    total_likes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tweet
        fields = "__all__"
