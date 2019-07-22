from django.db import models

# Create your models here.


class Person(models.Model):
    RELATIONSHIP_CHOICES = ((1, 'Husband'), (2, 'Wife'), (3, 'Own-child'), (4, 'Other-relative'), (5, 'Not-in-family'), (6, 'Unmarried'))
    SEX_CHOICES = (1, 'Male'), (2, 'Female')
    RACE_CHOICES = ((1,'White'), (2, 'Black'), (3, 'Asian-Pac-Islander'), (4, 'Amer-Indian-Eskimo'), (5, 'Other'))

    age = models.IntegerField()
    work = models.CharField(max_length=30)
    fnlwgt = models.IntegerField()
    education = models.CharField(max_length=30)
    education_num = models.IntegerField()
    marital_status = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    relationship = models.IntegerField(choices=RELATIONSHIP_CHOICES)
    race = models.IntegerField(choices=(RACE_CHOICES))
    sex = models.IntegerField(choices=(SEX_CHOICES))
    capital_gain = models.IntegerField()
    capital_loss = models.IntegerField()
    hours_per_week = models.IntegerField()
    native_country = models.CharField(max_length=30)
    salary = models.IntegerField()
    salary_range = models.CharField(max_length=5)