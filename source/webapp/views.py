from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from webapp.forms import MessageForm
from webapp.models import Message


class SendMessage(CreateView):
    model = Message
    template_name = 'massege/massege_create.html'
    form_class = MessageForm

    def form_valid(self, form):
        recipient_id = self.kwargs.get('id')
        print(recipient_id)
        recipient = get_user_model().objects.get(pk=recipient_id)
        message = form.save(commit=False)
        message.author = self.request.user
        message.recipient = recipient
        message.save()
        return redirect('users')
