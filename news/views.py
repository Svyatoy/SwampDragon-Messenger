from __future__ import unicode_literals

# from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import *
from news.models import News


class ListNewsView(ListView):
    model = News
    paginate_by = 3
    template_name = 'news_list.html'


class UpdateNewsView(UpdateView):

    # def test_func(self):
    #     if self.request.user.is_authenticated():
    #         if self.request.user.is_staff:
    #             return True
    #         else:
    #             raise PermissionDenied
    #     else:
    #         return False

    model = News
    fields = '__all__'
    template_name = 'edit_news.html'

    def get_success_url(self):
        return reverse('resent-news')

    def get_context_data(self, **kwargs):
        context = super(UpdateNewsView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-news',
                                    kwargs={'pk': self.get_object().id})
        return context


class CreateNewsView(CreateView):

    # def test_func(self):
    #     if self.request.user.is_authenticated():
    #         if self.request.user.is_staff:
    #             return True
    #         else:
    #             raise PermissionDenied
    #     else:
    #         return False

    model = News
    fields = ['title', 'description', 'author']
    template_name = 'edit_news.html'

    def get_success_url(self):
        return reverse('resent-news')

    def get_context_data(self, **kwargs):

        context = super(CreateNewsView, self).get_context_data(**kwargs)
        context['action'] = reverse('add-news')

        return context


class NewsView(DetailView):
    model = News
    template_name = 'news.html'


class DeleteNewsView(DeleteView):

    # def test_func(self):
    #     if self.request.user.is_authenticated():
    #         if self.request.user.is_staff:
    #             return True
    #         else:
    #             raise PermissionDenied
    #     else:
    #         return False

    model = News
    template_name = 'delete_news.html'

    def get_success_url(self):
        return reverse('resent-news')
