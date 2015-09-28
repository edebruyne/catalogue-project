from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    brand = models.ForeignKey('Brand')
    category = models.ForeignKey('Category')
    price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ('name',)

class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ('name',)

class Brand(models.Model):
    name = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ('name',)


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand')