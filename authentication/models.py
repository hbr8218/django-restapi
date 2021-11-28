from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#### Extending auth user 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fav_genres = models.CharField(max_length=200, blank=True)
