from django.contrib.auth.models import User
from django.db import models


class Hall(models.Model):
    city = models.CharField('Місто', max_length=255)
    street = models.CharField('Вулиця', max_length=255)

    class Meta:
        verbose_name = 'Локація'
        verbose_name_plural = 'Локації'

    def __str__(self):
        return f'Локація: {self.city}, {self.street}'


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    is_coach = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Учасник'
        verbose_name_plural = 'Учасники'

    def __str__(self):
        return f'{self.user.get_full_name()}'


class Lesson(models.Model):
    hall = models.ForeignKey(Hall, related_name='lessons', on_delete=models.PROTECT)
    members = models.ManyToManyField(Member, related_name='lessons')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заняття'
        verbose_name_plural = 'Заняття'

    def __str__(self):
        return f'{self.hall} {self.date}'
