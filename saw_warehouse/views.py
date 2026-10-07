from django.shortcuts import render, redirect
from .models import Material
from .forms import MaterialForm

# Create your views here.

def material_list(request):
    materials = Material.objects.all()
    return render(request, "saw_warehouse/material_list.html", {'materials': materials})

def material_add(request):
    if request.method == "POST":
        # Передаем данные из формы в наш класс MaterialForm
        form = MaterialForm(request.POST)
        
        # Django сам проверит данные на ошибки (валидация)
        if form.is_valid():
            form.save()  # <-- МАГИЯ: Django сам создаст объект и сохранит его в БД!
            return redirect('material_list')
    else:
        # Если это обычный GET-запрос, создаем пустую форму
        form = MaterialForm()
    
    # Передаем форму в шаблон
    return render(request, 'saw_warehouse/material_add.html', {'form': form})