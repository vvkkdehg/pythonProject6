from django.db import models
from django.utils import timezone

class Curator(models.Model):
    first_name = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=20)

class Direction(models.Model):
    name = models.CharField(max_length=20)
    curator = models.ForeignKey(Curator,
                                on_delete=models.CASCADE ,
                                related_name='direction')