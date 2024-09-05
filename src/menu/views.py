from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from menu.models import MenuModel
from .forms import MenuForm
from plat.forms import PlatForm



# Create your views here.

#def index(request):
#    return render(request,'menu/index.html')  


def menu_view(request):
    return render(request,'menu/menus.html')  


def edit_menu_view(request, id):  
    menus = get_object_or_404(MenuModel, id=id)  
    
    if request.method == 'POST':

        form = MenuForm(request.POST, instance=menus)  
        if form.is_valid():
            form.save()  
            return redirect('menu:list') 
    else:
        form = UserForm(instance=menus) 
    context["form"] = form
    
    return render(request, 'menu/edit_form.html', context)



        

def add_menu_view(request):
    if request.method == "POST":
        menu_form = MenuForm(request.POST)
        plat_form = PlatForm(request.POST)

        if menu_form.is_valid() and plat_form.is_valid():
            plat_form = plat_form.save()
            menus = menu_form.save(commit=False)
            menus.plats = plat_form 
            menus.save()

            messages.success(request, 'menu added successfully!')
            return redirect('menus:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        menu_form = UserForm()
        plat_form = PlatForm()

    return render(request, 'html/forms.html', {'menu_form': menu_form, 'plat_form': plat_form})
