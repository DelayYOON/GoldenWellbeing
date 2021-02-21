from django.db import models
from core import models as core_models

# Create your models here.


class Lecture(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return f'{self.author}: {self.body}'


class Video(core_models.TimeStampedModel):
    """ Video Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="lecture_videos")
    lecture = models.ForeignKey(
        "Lecture", related_name="videos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
