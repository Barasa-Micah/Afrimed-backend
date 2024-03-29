from django.db import models

# Create your models here.

class Medics(models.Model):
    name = models.CharField(max_length = 200)
    medical_licence_number = models.IntegerField()
    place_of_practice = models.TextField()
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name