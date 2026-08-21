from django.db import models

# Create your models here.
class coustmers(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    designation=models.CharField(max_length=30)
    time=models.TimeField()

    def __str__(self):
        return self.name
