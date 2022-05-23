from django.db import models


class News(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField(blank=True)
    creat_up = models.DateTimeField(auto_now_add=True)
    update_up = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    is_publishen = models.BooleanField(default=True)