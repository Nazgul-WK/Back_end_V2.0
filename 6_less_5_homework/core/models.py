from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    group = models.CharField(max_length=150)



