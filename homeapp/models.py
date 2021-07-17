from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(blank=True, max_length=500)

    senderdevice = models.CharField(blank=True, max_length=50, default="def")
    senderos = models.CharField(blank=True, max_length=50, default="def")
    senderosversion = models.CharField(
        blank=True, max_length=50, default="def")
    senderbrowser = models.CharField(blank=True, max_length=50, default="def")
    senderbrowserversion = models.CharField(
        blank=True, max_length=50, default="def")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    userdevice = models.CharField(blank=True, max_length=50, default="def")
    useros = models.CharField(blank=True, max_length=50, default="def")
    userosversion = models.CharField(
        blank=True, max_length=50, default="def")
    userbrowser = models.CharField(blank=True, max_length=50, default="def")
    userbrowserversion = models.CharField(
        blank=True, max_length=50, default="def")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Activitylog(models.Model):
    user = models.CharField(blank=True, max_length=200, default="anonymous")
    activity = models.TextField(
        blank=True, max_length=250, default="no activity")
    message = models.CharField(blank=True, max_length=250)
    reflink = models.CharField(blank=True, max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
