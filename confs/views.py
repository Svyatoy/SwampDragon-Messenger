from datetime import timedelta

# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from confs.models import Conference
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, View


def home(request):
    return render(request, 'home.html')


class ListConferencesView(ListView):
    queryset = Conference.objects.filter(event_date__gte=datetime.today()-timedelta(3))
    paginate_by = 5
    template_name = 'conference_list.html'


class ListConferencesArchiveView(ListView):
    queryset = Conference.objects.filter(event_date__lte=datetime.today()-timedelta(3))
    template_name = 'conference_list.html'


class ConferenceView( DetailView):

    model = Conference
    template_name = 'conference.html'


class CreateConferenceView(CreateView):

    # def test_func(self):
    #     if self.request.user.is_authenticated():
    #         if self.request.user.is_staff:
    #             return True
    #         else:
    #             raise PermissionDenied
    #     else:
    #         return False

    model = Conference
    fields = ['title', 'place', 'description', 'event_date', 'deadline']
    template_name = 'edit_conference.html'

    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse('resent-confs')

    def get_context_data(self, **kwargs):

        context = super(CreateConferenceView, self).get_context_data(**kwargs)
        context['action'] = reverse('add-conference')

        return context


class UpdateConferenceView(UpdateView):

    # def test_func(self):
    #     if self.request.user.is_authenticated():
    #         if self.request.user.is_staff:
    #             return True
    #         else:
    #             raise PermissionDenied
    #     else:
    #         return False

    model = Conference
    fields = ['title', 'place', 'description', 'event_date', 'deadline']
    template_name = 'edit_conference.html'

    def get_success_url(self):
        return reverse('resent-confs')

    def get_context_data(self, **kwargs):
        context = super(UpdateConferenceView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-conference',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteConferenceView(DeleteView):
    #
    # def test_func(self):
    #     if self.request.user.is_authenticated():
    #         if self.request.user.is_staff:
    #             return True
    #         else:
    #             raise PermissionDenied
    #     else:
    #         return False

    model = Conference
    template_name = 'delete_conference.html'

    def get_success_url(self):
        return reverse('resent-confs')


class ConferenceRegister(View):

    @staticmethod
    def get(request, pk):
        conference = Conference.objects.get(pk=pk)
        if not conference.is_register_available():
            return HttpResponse('Registration is closed')

        reporter = request.user
        if reporter in conference.reporters.all():
            return HttpResponse('You already have been registered')

        conference.reporters.add(reporter)

        return HttpResponse('Registration completed')


class ConferenceSubscribe(View):

    @staticmethod
    def get(request, pk):
        conference = Conference.objects.get(pk=pk)
        if not conference.is_register_available():
            return HttpResponse('Registration is closed')

        listener = request.user
        if listener in conference.listeners.all():
            return HttpResponse('You already have been subscribed')

        if listener in conference.reporters.all():
            return HttpResponse('You already have been registered')

        conference.listeners.add(listener)

        return HttpResponse('Registration completed')
