from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

from webapp.forms import MessageForm
from webapp.models import Message


class SendMessage(LoginRequiredMixin, CreateView):
    model = Message
    template_name = 'massege/massege_create.html'
    form_class = MessageForm

    def form_valid(self, form):
        recipient_id = self.kwargs.get('id')
        recipient = get_user_model().objects.get(pk=recipient_id)
        message = form.save(commit=False)
        message.author = self.request.user
        message.recipient = recipient
        message.save()
        return redirect('all_messages')


class AllMessage(ListView):
    template_name = 'massege/all_messages.html'
    context_object_name = 'messages'
    model = Message
    paginate_by = 5
    paginate_orphans = 1
    ordering = ['-sent_time']
