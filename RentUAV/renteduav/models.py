from django.db import models
from audioop import reverse

# Create your models here.



class RentedUavs(models.Model):
    uav = models.CharField(max_length=20, blank=False )
    date = models.DateField(blank=False,null=False )
    member = models.CharField(max_length=200,blank=False )


def get_absolute_url(self):
        return reverse('renteduav-detail', kwargs={'pk': self.pk})