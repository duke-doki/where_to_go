from django.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField(
        'Место',
        max_length=100
    )
    description_short = models.TextField(
        'Короткое описание',
        null=True, blank=True
    )
    description_long = models.TextField(
        'Длинное описание',
        null=True, blank=True
    )
    coordinates = models.JSONField(
        'Координаты',
        null=True, blank=True
    )

    def __str__(self):
        return self.title
