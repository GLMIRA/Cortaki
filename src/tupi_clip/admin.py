from django.contrib import admin
from .models import Video, Chapter


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "channel",
        "status",
        "file",
    )
    list_filter = ("status",)
    search_fields = (
        "title",
        "channel",
    )


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "video__title",
        "status",
        "start_time",
        "end_time",
        "file",
    )
    list_filter = ("status",)
    search_fields = (
        "title",
        "video__title",
    )

    def video_title(self, obj):
        return obj.video.title

    video_title.short_description = "Video Title"
