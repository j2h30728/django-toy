from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_users),
    path("<int:user_id>", views.get_user_detail),
    path("<int:user_id>/tweets", views.get_all_tweets_written_by_user),
]
