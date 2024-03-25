from django.shortcuts import render

# Create your views here.

# ChatRoom
## chatRoomList
# api/v1/chat
## [GET] : 전체 채팅방 조회
## [POST] : 채팅방 생성


# ChatRoomlist
## chatRoomList
## api/v1/chat/{room_id}
## [DELETE] : 해당 채팅방 삭제
## [PUT] : 채팅방 관련 수정 : 이름, 인원수 등
from .models import ChatRoom, ChatMessage
from .serializers import ChatRoomSerializer, ChatMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all()  # objs -> json (직렬화)
        serializer = ChatRoomSerializer(chatrooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data
        serializer = ChatRoomSerializer(
            data=user_data
        )  # 역직렬화 (json to django objects)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


# ChatMessage
## ChatMessageList
## api/v1/chat/{room_id}/messages
## [GET] : 채팅 내역 조회
## [POST] : 채팅 메세지 생성


from django.shortcuts import get_object_or_404


class ChatMessageList(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom)  # django objects
        # 직렬화
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        serializer = ChatMessageSerializer(data=request.data)  # json -> objects

        if serializer.is_valid():
            # serializer.save(chatroom)
            serializer.save(room=chatroom, sender=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_data = request.data
        chatroom = get_object_or_404(ChatRoom, id = room_id)

        serializer = ChatMessageSerializer(data = user_data)
        serializer.is_valid =(raise_exception=True)
        serializer.save(room=room, sender=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
