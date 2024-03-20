from rest_framework import serializers
from .models import Video
from users.serializers import UserSeiralizer
from comments.serializers import CommentSeiralizer


class VideoSerializer(serializers.ModelSerializer):

    user = UserSeiralizer(read_only=True)

    class Meta:
        model = Video
        fields = "__all__"
        # depth = 1

    comment = CommentSeiralizer(read_only=True)
