import companies
from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', companies.views.ListCompaniesView.as_view(),
        name='companies-list'),
    url(r'^(?P<pk>\d+)/$', companies.views.CompanyView.as_view(),
        name='company-view'),
    url(r'^new$', companies.views.CreateCompanyView.as_view(),
        name='add-company'),
    url(r'^edit/(?P<pk>\d+)/$', companies.views.UpdateCompanyView.as_view(),
        name='edit-company'),
    url(r'^delete/(?P<pk>\d+)/$', companies.views.DeleteCompanyView.as_view(),
        name='delete-company',),
]
