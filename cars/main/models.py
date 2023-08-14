from django.db import models

# Create your models here.


class Cars(models.Model):
    carname = models.CharField(max_length=50, default='abc')
    cardesc = models.CharField(max_length=1000, default='abc')
    carimage = models.ImageField(
        upload_to='media/images', default="cars/media/images/pizza-g8b47044f6_1280.jpg")

    def __str__(self) -> str:
        return self.carname
