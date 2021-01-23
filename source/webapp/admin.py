from django.contrib import admin

from webapp.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'message', 'author', 'recipient', 'sent_time',)


admin.site.register(Message, MessageAdmin)

