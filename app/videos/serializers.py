from rest_framework import serializers
from .models import Video
from users.serializers import UserSeiralizer
from comments.serializers import CommentSerializer


class VideoListSerializer(serializers.ModelSerializer):

    # Video(FK) -> User
    user = UserSeiralizer(read_only=True)

    class Meta:
        model = Video
        fields = "__all__"
        # depth = 1


class VideoDetailSerializer(serializers.ModelSerializer):

    # Video(FK) -> User
    user = UserSeiralizer(read_only=True)

    # Video -> Comment(FK)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = "__all__"
        # depth = 1
