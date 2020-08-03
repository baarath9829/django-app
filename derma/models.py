from django.db import models

# Create your models here.
class input(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=30)
    image  = models.ImageField(upload_to="uploads/")
