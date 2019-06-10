# coding: utf8
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from kvadra.settings import MEDIA_URL


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(_(u'avatar'), upload_to='avatar', blank=True, max_length=1000)
    # Добавляем поле дня рождения.
    birthday = models.DateField(_(u'birthday'), blank=True, null=True)
    # username = models.CharField(max_length=150, unique=True)
    id_telegramm = models.BigIntegerField(null=True, blank=True, default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profileuser.save()
