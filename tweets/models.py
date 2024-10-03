from django.db import models
from users.models import User


class Tweet(models.Model):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="tweets"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tweet(payload={self.payload} / like_count={self.likes.count()} / author={self.user.pk};{self.user.name})"

    def total_likes_count(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Like(user={self.user.name} / tweet={self.tweet.payload})"
