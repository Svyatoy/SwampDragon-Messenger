from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from login.forms import *
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


class UpdateUserView(UpdateView):
    model = User

    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'edit_user.html'

    def get_success_url(self):
        return reverse('resent-confs')

    def get_context_data(self, **kwargs):
        context = super(UpdateUserView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-user',
                                    kwargs={'pk': self.get_object().id})
        return context


class UserAccountView(DetailView):
    model = User
    template_name = 'user_show.html'


class UserView(View):
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    @staticmethod
    def get(request):

        # user = get_object_or_404(User, pk=user_id)
        user = request.user

        context = {
            'user_id': user.id,
            'username': user.username,
            'email': user.email,

            'conferences_listener': user.conf_listener.all(),
            'conferences_reporter': user.conf_reporter.all(),
        }

        return render(request, 'user_show.html', context)

    # def get_queryset(self):
    #     user = self.request.user
    #     return user

    template_name = 'user_show.html'
#
#
# class UpdateUserView(UpdateView):
#     model = Conference
#     fields = ['title', 'place', 'description', 'event_date', 'deadline']
#     template_name = 'edit_conference.html'
#
#     def get_success_url(self):
#         return reverse('resent-confs')
#
#     def get_context_data(self, **kwargs):
#         context = super(UpdateConferenceView, self).get_context_data(**kwargs)
#         context['action'] = reverse('edit-conference',
#                                     kwargs={'pk': self.get_object().id})
#         return context


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )


def register_success(request):
    return render_to_response(
        'registration/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
