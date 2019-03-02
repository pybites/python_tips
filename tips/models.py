from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tip(models.Model):
    tip = models.TextField()
    code = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    # set by admin
    approved = models.BooleanField(default=False)
    share_link = models.URLField(blank=True, null=True)

    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Author(models.Model):
    """Extending the standard User model:
       https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slack_handle = models.CharField(max_length=30, unique=True)
    twitter_handle = models.CharField(max_length=30)


@receiver(post_save, sender=User)
def create_user_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_author(sender, instance, **kwargs):
    instance.author.save()
