from django.db import models


class Rot(models.Model):
    rot = models.IntegerField(verbose_name='Сдвиг')
    amount = models.IntegerField(default=0, verbose_name='Количество запрсосов')

    class Meta:
        verbose_name = 'Rot'
        verbose_name_plural = 'Rots'
        ordering = ['-amount']
