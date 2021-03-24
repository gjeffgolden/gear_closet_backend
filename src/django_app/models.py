from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class User(AbstractUser):
    hometown = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username}'


class Item(models.Model):
    nickname = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    model_year = models.PositiveIntegerField(
        default=2021,
        validators=[
            MaxValueValidator(2050),
            MinValueValidator(1950)
        ]
    )
    item_type = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    image_url = models.CharField(max_length=500)
    retired = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="items", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nickname}'

