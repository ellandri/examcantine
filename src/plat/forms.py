from django import forms
from menu.models import PlatModel


class PlatForm(forms.ModelForm):
 class Meta:
    model= PlatModel
    fields=["name","summary"]
   
