from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender = models.Choices('male', 'female')
    weight = models.PositiveIntegerField(default=0)

# pythom3 manage.py makemigrations
# python3 manage.py migrate