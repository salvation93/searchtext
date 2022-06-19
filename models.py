from django.db import models

# Create your models here.
class Articles(models.Model):
    topic = models.CharField(max_length=240, null = False)
    body = models.TextField(null=False)
    author = models.CharField(max_length=40, null=False)
    time = models.DateTimeField(auto_now_add = True)