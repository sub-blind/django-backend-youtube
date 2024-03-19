from django.db import models
from users.models import User
from commons.models import CommonModel


class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=30)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField()  # S3 Bucket -> Save file -> URL -> Save URL
    video_file = models.FileField(upload_to="storage/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
