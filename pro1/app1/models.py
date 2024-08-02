from django.db import models
from django.core import validators

def titleCap(s):
    print(s.istitle())
    if s.istitle()==False:
        validators.ValidationError(message='Please enter 1st letter of every word in capital')


# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, validators=[titleCap])
    director = models.CharField(max_length=100, validators=[titleCap])
    review = models.CharField(max_length=100000000)
    rating = models.CharField(max_length=23)
    created_at = models.DateField(auto_now_add=True)
    email = models.EmailField()
    status = models.CharField(max_length=23)
    genre = models.CharField(max_length=24)