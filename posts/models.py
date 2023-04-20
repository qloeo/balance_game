from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    select1_users = models.IntegerField(default=0)
    select1_content = models.CharField(max_length=80)
    select2_users = models.IntegerField(default=0)
    select2_content = models.CharField(max_length=80)
    answered = models.BooleanField(default=False)
