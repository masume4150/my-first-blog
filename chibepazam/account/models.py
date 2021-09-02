from django.db import models
from core.models import Common
# Create your models here.


class AboutUs(Common):
    home = models.CharField(("خانه"), max_length=50)
    call = models.CharField(("شماره تماس"), max_length=11)

    def __str__(self):
        return self.home
