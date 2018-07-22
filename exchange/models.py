from django.db import models


# Create your models here.

class Exchange(models.Model):
    vef = models.FloatField()
    cny = models.FloatField()
    time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return '{}/{} @ {}'.format(self.vef, self.cny, self.time.strftime('%Y-%m-%d %H:%M:%S %z %Z'))
