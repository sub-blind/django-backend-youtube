from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubSerializer
from django.shortcuts import get_object_or_404
from .models import Subscription
from rest_framework import status
from rest_framework.exceptions import NotFound


class SubscriptionList(APIView):
    def get(self, request):
        subs = Subscription.objects.filter(subscriber=request.user)
        serializer = SubSerializer(subs, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_data = request.data  # json -> object (Serializer)
        serializer = SubSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, status=201)


class SubscriptionDetail(APIView):
    def get(self, request, pk):
        subs = Subscription.objects.filter(subscribed_to=pk)
        serializer = SubSerializer(subs, many=True)

        return Response(serializer.data)

    def delete(self, request, pk):

        subs = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        subs.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
