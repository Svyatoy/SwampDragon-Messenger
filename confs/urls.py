import confs
from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', confs.views.ListConferencesView.as_view(), name='resent-confs'),
    url(r'^archive/$', confs.views.ListConferencesArchiveView.as_view(), name='archive-confs'),

    url(r'^(?P<pk>\d+)/$', confs.views.ConferenceView.as_view(), name='conference-view'),

    url(r'^new$', confs.views.CreateConferenceView.as_view(), name='add-conference'),
    url(r'^edit/(?P<pk>\d+)/$', confs.views.UpdateConferenceView.as_view(), name='edit-conference'),
    url(r'^delete/(?P<pk>\d+)/$', confs.views.DeleteConferenceView.as_view(), name='delete-conference'),

    url(r'^(?P<pk>\d+)/subscribe/$', confs.views.ConferenceSubscribe.as_view(), name='conference-subscribe'),
    url(r'^(?P<pk>\d+)/register/$', confs.views.ConferenceRegister.as_view(), name='conference-register'),
]
