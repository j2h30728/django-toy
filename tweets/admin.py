from django.contrib import admin
from .models import Like, Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Data",
            {
                "fields": (
                    "id",
                    "payload",
                    "user",
                    "total_likes_count",
                    "created_at",
                    "updated_at",
                ),
                "classes": ("wide",),
            },
        ),
    )

    list_display = (
        "id",
        "user",
        "payload",
        "total_likes_count",
        "created_at",
    )
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Data",
            {
                "fields": (
                    "id",
                    "user",
                    "tweet",
                    "created_at",
                    "updated_at",
                ),
                "classes": ("wide",),
            },
        ),
    )

    list_display = ("id", "user", "tweet", "created_at")
    readonly_fields = ("id", "created_at", "updated_at")
