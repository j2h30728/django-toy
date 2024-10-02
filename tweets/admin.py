from django.contrib import admin
from .models import Like, Tweet


class ElonMuskFilter(admin.SimpleListFilter):
    title = "Elon Musk"
    parameter_name = "elon_musk"

    def lookups(self, request, model_admin):
        return [(True, "Contain 'Elon Musk'"), (False, f"Don't contain 'Elon Musk'")]

    def queryset(self, request, queryset):
        isContainElonMusk = self.value()
        ELON_MUSK = "Elon Musk"
        if isContainElonMusk == "True":
            return queryset.filter(payload__contains=ELON_MUSK)
        elif isContainElonMusk == "False":
            return queryset.exclude(payload__contains=ELON_MUSK)
        else:
            queryset


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
                    "created_at",
                    "updated_at",
                ),
                "classes": ("wide",),
            },
        ),
    )
    search_fields = (
        "payload",
        "user__username",
    )
    list_filter = (
        ElonMuskFilter,
        "created_at",
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
    search_fields = ("user__username",)
    list_filter = ("created_at",)
    list_display = ("id", "user", "tweet", "created_at")
    readonly_fields = ("id", "created_at", "updated_at")
