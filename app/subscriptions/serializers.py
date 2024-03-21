from rest_framework import serializers
from .models import Subscription


class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

    def validate(self, data):  # data : type[dict]
        if data["subscriber"] == data["subscribed_to"]:
            raise serializers.ValidationError("You can't subscribe to yourself")

        return data
