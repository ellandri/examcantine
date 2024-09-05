from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from plat.models import PlatModel
from menu.forms import MenuForm
from .forms import PlatForm



# Create your views here.



def plat_view(request):
    return render(request,'plat/plats.html')  
#   search_field = request.GET.get('search')
#    if search_field :
 #       menus = UserModel.objects.filter(plat__icontains=search_field)
 #       context = {
 #           'menus': menus,
 #           'search_field': search_field,
  #      }
#    else:
#        menus = MenuModel.objects.all() 
#        context = {
#            'menus': menus,
#        }
#    return render(request, 'html/menus.html',context)


def edit_plat_view(request, id):  
    plats = get_object_or_404(PlatModel, id=id)  
    
    if request.method == 'POST':

        form = PlatForm(request.POST, instance=plats)  
        if form.is_valid():
            form.save()  
            return redirect('plat:list') 
    else:
        form = PlatForm(instance=plats) 
    context["form"] = form
    
    return render(request, 'plat/edit_form.html', context)



        

def add_plat_view(request):
    if request.method == "POST":
        plat_form = PlatForm(request.POST)

        if menu_form.is_valid() and plat_form.is_valid():
            plat_form = plat_form.save()
            plat_form.save()

            messages.success(request, 'plat added successfully!')
            return redirect('plat:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        plat_form = PlatForm()

    return render(request, 'html/forms.html', {'plat_form': plat_form})
