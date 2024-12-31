import os
from typing import TYPE_CHECKING

from celery import Celery
from celery.utils.log import get_task_logger
from django.conf import settings
from django.apps import apps
from pytubefix import YouTube

logger = get_task_logger(__name__)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tupi_cut.settings")

app = Celery()
app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True)
def hello_word(self):

    print("-------------------------------------------> Vai Brasil!!!")


@app.task(bind=True)
def download_video(self, video_new_pk):
    from . import models

    logger.info("start download video task")
    try:
        video_new = models.Video.objects.get(pk=video_new_pk)
        youtube_client = YouTube(url=video_new.url)
        youtube_session = youtube_client.streams.get_highest_resolution()
        file_video_name = youtube_session.download("./video")
        logger.info(f"dowloaded video {video_new} in {file_video_name}")
        video_new.file = file_video_name
        video_new.status = models.PROCESSED
        video_new.save()
        logger.info(f"finish dowload video {video_new}")
    except Exception:
        logger.error(f"Error on dowload video task", exc_info=True)
        self.retry()


@app.task(bind=True)
def select_video_to_download(self):
    from . import models

    query_set = models.Video.objects.filter(status=models.NEW)
    logger.debug(f"Get {len(query_set)} videos to process")
    if len(query_set) > 0:
        video_new = query_set[0]
        logger.info(f"process video {video_new.title}")
        video_new.status = models.IN_PROCESS
        video_new.save()
        download_video.delay(video_new.pk)
    else:
        logger.info("No video to process")

    
    query_set = models.Chapter.objects.filter(status=models.NEW)
    for chapter in query_set:
        if chapter.video.status == models.NEW:
            chapter.status = in progress
            fatia.delay(chapter.pk)
