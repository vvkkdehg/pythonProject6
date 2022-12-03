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

class Group(models.Model):
    number = models.CharField(max_length=20)
    deviz = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    direction = models.ForeignKey(Direction,
                                  on_delete=models.CASCADE,
                                  related_name='group')
    def __str__(self):
        return 'group '+self.number +'('+str(self.id)+')'

class Disciplina(models.Model):
    name = models.CharField(max_length=50)
    lessons = models.CharField(max_length=20)
    homework = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    direction = models.ForeignKey(Direction,
                                  on_delete=models.CASCADE,
                                  related_name='disciplina')

class Student(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    otchesvo = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    group = models.ForeignKey(Group,
                                  on_delete=models.CASCADE,
                                  related_name='student')
