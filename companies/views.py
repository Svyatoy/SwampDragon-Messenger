# from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from companies.models import Company
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView


class ListCompaniesView(ListView):
    model = Company
    # paginate_by = 2
    template_name = 'companies_list.html'


class CompanyView(DetailView):
    model = Company
    template_name = 'company.html'


class CreateCompanyView(CreateView):

    # def test_func(self):
    #     if self.request.user.is_authenticated():
    #         if self.request.user.is_staff:
    #             return True
    #         else:
    #             raise PermissionDenied
    #     else:
    #         return False

    model = Company
    fields = ['name', 'email', 'description']
    template_name = 'edit_company.html'

    def get_success_url(self):
        return reverse('companies-list')

    def get_context_data(self, **kwargs):

        context = super(CreateCompanyView, self).get_context_data(**kwargs)
        context['action'] = reverse('add-company')

        return context


class UpdateCompanyView(UpdateView):

    # def test_func(self):
    #     if self.request.user.is_authenticated():
    #         if self.request.user.is_staff:
    #             return True
    #         else:
    #             raise PermissionDenied
    #     else:
    #         return False

    model = Company
    fields = '__all__'
    template_name = 'edit_company.html'

    def get_success_url(self):
        return reverse('companies-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateCompanyView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-company',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteCompanyView(DeleteView):
    #
    # def test_func(self):
    #     if self.request.user.is_authenticated():
    #         if self.request.user.is_staff:
    #             return True
    #         else:
    #             raise PermissionDenied
    #     else:
    #         return False

    model = Company
    template_name = 'delete_company.html'

    def get_success_url(self):
        return reverse('companies-list')
