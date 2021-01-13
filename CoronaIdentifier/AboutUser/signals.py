from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyResult
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def post_save_create_result(sender, instance, created, **kwargs):
    if created:
        MyResult.objects.create(user=instance)
