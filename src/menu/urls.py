from django.urls import path
from .views import menu_view,add_menu_view,edit_menu_view

app_name='menu'

urlpatterns = [
#   path('', index, name='index'),
   path('', menu_view, name='list'),
    path('addm/', add_menu_view, name='add'),
    path('editm/<int:id>/', edit_menu_view, name='edit'),
    
]
