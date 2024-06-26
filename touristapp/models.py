from django.db import models

# Create your models here.

class tour_destinations(models.Model):
    name=models.CharField(max_length=200)
    destination_img=models.ImageField(upload_to='destination_img/')
    district=models.CharField(max_length=300)
    state=models.CharField(max_length=300)
    map_link=models.URLField(max_length=700)
    weather=models.CharField(max_length=200)
    description=models.CharField(max_length=900)


    def __str__(self):
        return '{}' .format(self.name)
