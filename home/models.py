from django.db import models


# Create your models here.


class Team_members(models.Model):
    name = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    image = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ' Add Member'
        ordering = ['name']


class Sections(models.Model):
    name = models.CharField(max_length=25, verbose_name='Section Name')

    def __str__(self):
        return self.name
