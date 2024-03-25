from rest_framework.serializers import Modelserializer
from .models import ChatRoom, ChatMessage


class ChatRoomSerializer(Modelserializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"


class ChatMessageSerializer(Modelserializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"
        read_only_fields = ["room", "sender"]
        depth = 1
