from django.db import models

# Create your models here.
class input(models.Model):
    label = models.CharField(max_length=30)
    image  = models.ImageField(upload_to="uploads/")
