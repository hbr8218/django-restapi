from django.db import models
from django.contrib.auth.models import User
from random import randint
import datetime
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=300)
    release_date = models.DateField(null=True, blank=True)
    up_votes = models.IntegerField(null=True, blank=True)
    down_votes = models.IntegerField(null=True, blank=True)
    reviews = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.field3 = self._randomDate(2000,2022)
        super(Movie, self).save(*args, **kwargs)

    def _randomDate(self,start_year, end_year):
        return datetime.date(randint(start_year,end_year), randint(1,12),randint(1,28))

    class Meta:
        db_table = 'movie'

    def __str__(self) -> str:
        return self.title
