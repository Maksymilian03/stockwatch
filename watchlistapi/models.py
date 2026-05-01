from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=16)
    add_date = models.DateTimeField(auto_now_add=True)
    describe = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user} - {self.name}({self.symbol})"




