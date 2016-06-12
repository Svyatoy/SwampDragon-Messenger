from django.core.urlresolvers import reverse
from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from messanges.models import Message


class ListMessagesView(ListView):

    template_name = 'messages_list.html'

    def get_queryset(self):
        mailbox = Message.objects.filter(Q(receiver_id__exact=self.request.user.id) | Q(sender_id__exact=self.request.user.id))
        return mailbox


class MessageView(DetailView):

    model = Message
    template_name = 'message.html'

    def get_object(self, queryset=None):
        object = super(MessageView, self).get_object()

        object.read = False
        object.save()

        return object


class CreateMessageView(CreateView):
    model = Message
    fields = ['receiver', 'text']
    template_name = 'message_create.html'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        # email = form.instance.receiver.email
        #
        # send_mail(
        #     'New message',
        #     'Someone wrote you a messages at conference.lab',
        #     'admin@conference.lab',
        #     [email],
        #     fail_silently=False,
        # )

        return super(CreateMessageView, self).form_valid(form)

    def get_success_url(self):
        return reverse('messages')

    def get_context_data(self, **kwargs):

        context = super(CreateMessageView, self).get_context_data(**kwargs)
        context['action'] = reverse('add-message')

        return context


class UpdateMessageView(UpdateView):

    model = Message
    fields = ['text']
    template_name = 'message_create.html'

    def get_success_url(self):
        return reverse('messages')

    def get_context_data(self, **kwargs):
        context = super(UpdateMessageView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-message',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteMessageView(DeleteView):

    model = Message
    template_name = 'message_delete.html'

    def get_success_url(self):
        return reverse('messages')
