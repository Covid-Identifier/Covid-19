from django.db import models
from django.contrib.auth.models import User

class MyResult(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    result = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)
