import news
from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', news.views.ListNewsView.as_view(),
        name='resent-news'),
    url(r'^(?P<pk>\d+)/$', news.views.NewsView.as_view(),
        name='news-view'),
    url(r'^new$', news.views.CreateNewsView.as_view(),
        name='add-news'),
    url(r'^edit/(?P<pk>\d+)/$', news.views.UpdateNewsView.as_view(),
        name='edit-news'),
    url(r'^delete/(?P<pk>\d+)/$', news.views.DeleteNewsView.as_view(),
        name='delete-news',),
    #
    # url(r'^archive/$', news.views.ListNewsView.as_view(),
    #     name='archive-news'),
]
