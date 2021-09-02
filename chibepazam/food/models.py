from django.db import models
from core.models import Common
# Create your models here.


class Food(Common):
    name = models.CharField(max_length=70, unique=True)
    text = models.TextField(("مواد اولیه و توضیحات"))
    time = models.IntegerField()
    photo = models.ImageField(upload_to='foods/')

    def __str__(self):
        return self.name
