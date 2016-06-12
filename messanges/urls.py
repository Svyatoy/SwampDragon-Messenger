from django.conf.urls import url

from views import ListMessagesView, MessageView, CreateMessageView, DeleteMessageView, UpdateMessageView

urlpatterns = [

    url(r'^$', ListMessagesView.as_view(), name='messages'),
    url(r'^(?P<pk>\d+)$', MessageView.as_view(), name='message'),
    url(r'^new/$', CreateMessageView.as_view(), name='add-message'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteMessageView.as_view(), name='delete-message'),
    url(r'^edit/(?P<pk>\d+)/$', UpdateMessageView.as_view(), name='edit-message'),
]