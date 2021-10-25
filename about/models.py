from django.db import models
from django.db.models.aggregates import Max
from django.db.models.query_utils import check_rel_lookup_compatibility

# Create your models here.


class Head(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    educational_level = models.IntegerField()
    city = models.CharField(max_length=20)
    HeadWord = models.TextField(max_length=500)
    image = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ' Head Information'


class Info(models.Model):
    name = models.CharField(max_length=15)

    Who_We_are_URI = models.TextField(max_length=50000)

    What_Do_We_Care_about_Why_Did_URI_Stablish = models.TextField(
        max_length=50000)

    The_Goal_Of_Scientific_Research = models.TextField(max_length=50000)

    The_Goal_Of_Scientific_Research_2 = models.TextField(
        max_length=50000, null=True, blank=True)

    The_Goal_Of_Scientific_Research_3 = models.TextField(
        max_length=50000, null=True, blank=True)

    The_Goal_Of_Scientific_Research_4 = models.TextField(
        max_length=50000, null=True, blank=True)

    The_Goal_Of_Scientific_Research_5 = models.TextField(
        max_length=50000, null=True, blank=True)

    The_Goal_Of_Scientific_Research_6 = models.TextField(
        max_length=50000, null=True, blank=True)

    The_Goal_Of_Scientific_Research_7 = models.TextField(
        max_length=50000, null=True, blank=True)

    The_Goal_Of_Scientific_Research_8 = models.TextField(
        max_length=50000, null=True, blank=True)

    The_Goal_Of_Scientific_Research_9 = models.TextField(
        max_length=50000, null=True, blank=True)

    The_Goal_Of_Scientific_Research_10 = models.TextField(
        max_length=50000, null=True, blank=True)

    What_Will_You_Benefit_From_URI = models.TextField(max_length=50000)
    Beginning_Of_The_Story = models.TextField(max_length=50000)

    class Meta:
        verbose_name = ' URI Information'

    def __str__(self):
        return self.name
