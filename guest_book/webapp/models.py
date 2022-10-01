from django.db import models
from django.db.models import TextChoices



class StatusChoices(TextChoices):
    ACTIVE = 'active', 'Активно'
    BLOCKED = 'blocked', 'Заблокировано'


class GuestBook(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(max_length=200, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст записи')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=30, null=False, blank=False, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)


    def __str__(self) -> str:
        return f'{self.author} - {self.email} - {self.text}'