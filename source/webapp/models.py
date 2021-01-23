from django.db import models
from django.contrib.auth import get_user_model


class Message(models.Model):
    message = models.TextField(max_length=2000, verbose_name='Сообщение')
    author = models.ForeignKey(get_user_model(), related_name='author_message', default=1,
                               on_delete=models.SET_DEFAULT, verbose_name='Автор')
    recipient = models.ForeignKey(get_user_model(), related_name='recipient_message', default=1,
                                  on_delete=models.SET_DEFAULT, verbose_name='Получатель')
    sent_time = models.DateTimeField(auto_now_add=True,verbose_name='Время отправления')

    def __str__(self):
        return f'{self.author} - {self.message}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
