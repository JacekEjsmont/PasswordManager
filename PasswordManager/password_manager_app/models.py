from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Entry(models.Model):
    site_name = models.CharField(max_length=20)
    site_url = models.URLField()
    login_name = models.CharField(max_length=20)
    login_password = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.site_name
