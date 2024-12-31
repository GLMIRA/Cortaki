# TODO: Mudar tudo para ingles!!!

import os

from django.db import models

NEW = "000"
IN_PROCESS = "100"
PROCESSED = "200"
ERROR = "900"
STATUS_CHOICES = {
    NEW: "New",
    IN_PROCESS: "In Process",
    PROCESSED: "Processed",
    ERROR: "Error",
}


class Video(models.Model):
    url = models.URLField(
        verbose_name="Url do Video",
        null=False,
        blank=False,
    )
    title = models.CharField(
        verbose_name="Nome do Video",
        max_length=400,
        blank=False,
        null=False,
    )
    channel = models.CharField(
        verbose_name="Nome do Canal do Video",
        max_length=200,
        blank=False,
        null=False,
    )
    file = models.CharField(
        verbose_name="Downloaded File",
        max_length=200,
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=NEW,
    )

    def __str__(self):
        return f"{self.title} - {self.channel}"


class Chapter(models.Model):
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
    )

    start_time = models.DurationField(
        verbose_name="Start Time Chapter",
        blank=False,
        null=False,
    )

    end_time = models.DurationField(
        verbose_name="End Time Chapter",
        blank=False,
        null=False,
    )
    title = models.CharField(
        verbose_name="Nome do Capitulo",
        max_length=400,
        blank=False,
        null=False,
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=NEW,
    )

    def __str__(self):
        return f"{self.video.title} - {self.title}"
