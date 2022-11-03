from django.db import models


class Rot(models.Model):
    rot = models.IntegerField(verbose_name='Сдвиг')
    usages = models.IntegerField(default=1, verbose_name='Количество запросов')

    class Meta:
        verbose_name = 'Rot'
        verbose_name_plural = 'Rots'
        ordering = ['-usages']
