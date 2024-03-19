from django.db import models
from users.models import User
from videos.models import Video


class LikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)  # True for like, False for dislike
