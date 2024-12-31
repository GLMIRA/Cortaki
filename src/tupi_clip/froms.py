from .models import Video, Chapter
from django import forms


class FormVideo(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            "url",
            "title",
            "chanel",
            "file",
            "status",
        ]


class FormChapter(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = [
            "video",
            "start_time",
            "end_time",
            "title",
            "file",
            "status",
        ]
