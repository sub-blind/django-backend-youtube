from django.db import models
from commons.models import CommonModel
from users.models import User
from videos.models import Video


# Create your models here.
class Comment(CommonModel):
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # User:Comment -> 1:N
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Video:Comment -> 1:N
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
