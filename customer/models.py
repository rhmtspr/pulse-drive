from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    profile_img = models.ImageField(upload_to="customer", blank=True, null=True)

    def __str__(self):
        return self.fullname
    
    class Meta: 
        verbose_name_plural = "Customer"