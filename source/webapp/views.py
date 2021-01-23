from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages = self.object_list
        messages_list, page, is_paginated = self.paginate_comments_send(messages)
        messages_list_recive, page_r, is_paginated_r = self.paginate_comments_recive(messages)
        context['messages_list'] = messages_list
        context['messages_list_recive'] = messages_list_recive
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        context['page_obj_r'] = page_r
        context['is_paginated_r'] = is_paginated_r
        return context

    def paginate_comments_send(self, messages):
        try:
            messages = messages.filter(author=self.request.user)
            if messages.count() > 0:
                paginator = Paginator(messages, self.paginate_by, orphans=self.paginate_orphans)
                page = paginator.get_page(self.request.GET.get('page', 1))
                is_paginated = paginator.num_pages > 1
                return page.object_list, page, is_paginated
            else:
                return messages, None, False
        except:
            return messages, None, False

    def paginate_comments_recive(self, messages):
        try:
            messages = messages.filter(recipient=self.request.user)
            if messages.count() > 0:
                paginator = Paginator(messages, self.paginate_by, orphans=self.paginate_orphans)
                page = paginator.get_page(self.request.GET.get('page', 1))
                is_paginated = paginator.num_pages > 1
                return page.object_list, page, is_paginated
            else:
                return messages, None, False
        except:
            return messages, None, False
