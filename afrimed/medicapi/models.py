from django.db import models

# Create your models here.

class Medics(models.Model):
    
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    
    name = models.CharField(max_length = 200)
    medical_licence_number = models.IntegerField()
    place_of_practice = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES ) 

    def __str__(self) -> str:
        return self.name
    
