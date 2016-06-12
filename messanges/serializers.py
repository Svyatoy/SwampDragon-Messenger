from swampdragon.serializers.model_serializer import ModelSerializer


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = 'messanges.Message'
        publish_fields = ['id', 'sender_id', 'receiver_id', 'text', 'read', 'ts_created']

