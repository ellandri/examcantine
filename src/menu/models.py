from django.db import models
from plat.models import PlatModel

class MenuModel(models.Model):
    plat = models.OneToOneField(PlatModel, on_delete=models.CASCADE, null=True, blank=True)  
    creation_date = models.DateField(auto_now_add=True)  

    def __str__(self):
        return self.creation_date 
