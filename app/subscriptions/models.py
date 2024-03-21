from django.db import models
from commons.models import CommonModel
from users.models import User


# Create your models here.
class Subscription(CommonModel):
    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    subscribed_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscribers"
    )
