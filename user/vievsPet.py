from django.shortcuts import render
from .models import PetsModel


# Create your views here.

def pet(request):
    qs = PetsModel.objects.all()

    return render(request, 'pet.html', {'pets_list': qs})
