
from audioop import reverse
from django.db import models

# Create your models here.
class Properties(models.Model):
    model = models.CharField(max_length=20, blank=False )
    brand = models.CharField(max_length=30,blank=False )
    weight = models.CharField(max_length=200,blank=False )
    category = models.CharField(max_length=30,blank=False)

    def get_absolute_url(self):
        return reverse('uav-detail', kwargs={'pk': self.pk})