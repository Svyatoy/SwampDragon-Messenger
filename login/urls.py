from django.conf.urls import url, include

from views import UserView, UserAccountView

urlpatterns = [
    url(r'^$', UserView.as_view(), name='user_profile'),
    url(r'^/edit$', UserView.as_view(), name='user_profile'),
    url(r'^users/(?P<pk>\d+)/$', UserAccountView.as_view(), name='user_account'),
    # url(r'^edit$', EditUserProfile.as_view(), name='edit_user_profile'),
    url(r'^messages/', include('messanges.urls')),
]
