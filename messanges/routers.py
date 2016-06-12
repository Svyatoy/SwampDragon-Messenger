from swampdragon.route_handler import register
from swampdragon.route_handler import ModelRouter
from models import Message
from serializers import NotificationSerializer


class NotificationRouter(ModelRouter):
    model = Message
    serializer_class = NotificationSerializer
    route_name = 'notifications'
    valid_verbs = ['subscribe']

register(NotificationRouter)
