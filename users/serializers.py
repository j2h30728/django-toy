from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    avatar = serializers.ImageField()
    name = serializers.CharField(max_length=150)
    gender = serializers.ChoiceField(choices=User.GenderChoices.choices)
