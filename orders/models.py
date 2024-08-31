from django.db import models
from django.contrib.auth.models import User
from ja.models import Ja


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ja = models.ForeignKey(Ja,on_delete=models.CASCADE)
    pric = models.IntegerField()
    paied = models.BooleanField(default=False)
    Create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


