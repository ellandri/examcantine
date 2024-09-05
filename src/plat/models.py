from django.db import models

class PlatModel(models.Model):
    name = models.CharField(max_length=100)  
    summary = models.TextField()  

    def __str__(self):
        return self.name 
