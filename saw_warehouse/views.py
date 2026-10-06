from django.shortcuts import render, redirect
from .models import Material

# Create your views here.

def material_list(request):
    materials = Material.objects.all()
    return render(request, "saw_warehouse/material_list.html", {'materials': materials})

def material_add(request):
    if request.method == "POST":
        material = Material()
        material.name = request.POST.get('material_name')
        material.quantity = request.POST.get('material_quantity')
        material.save()
        return redirect ('material_list')
    else:
        return render(request, 'saw_warehouse/material_add.html')
