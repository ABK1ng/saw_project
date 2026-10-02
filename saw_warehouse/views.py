from django.shortcuts import render
from .models import Material

# Create your views here.

def material_list(request):
    materials = Material.objects.all()
    return render(request, "saw_warehouse/material_list.html", {'materials': materials})
