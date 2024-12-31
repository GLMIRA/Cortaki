from django.contrib import admin
from .models import Video, Chapter

admin.site.register(
    [
        Video,
        Chapter,
    ]
)
