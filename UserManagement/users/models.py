from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100,null=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=10, choices=[('Male','Male'), ('Female','Female'), ('Other','Other')])
    mobile_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

