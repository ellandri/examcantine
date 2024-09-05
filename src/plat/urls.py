from django.urls import path
from .views import plat_view,add_plat_view,edit_plat_view

app_name='plat'

urlpatterns = [
   path('plat/', plat_view, name='list'),
    path('addp/', add_plat_view, name='add'),
    path('editp/<int:id>/', edit_plat_view, name='edit'),
    
]
