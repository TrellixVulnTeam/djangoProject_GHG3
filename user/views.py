
from .models import UsersModel
from django.shortcuts import render
from .models import PetsModel
from .forms import UserModel
from .forms import PetModel


def pet(request, id):
    qs = UsersModel.objects.get(pk=id).ovners.all()
    form = PetModel(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'pet.html', {'pets_list': qs, 'form': form})



def name_list(request):
    qs = UsersModel.objects.all()
    form = UserModel(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'user.html', {'names_list': qs, 'form': form})

def calculator(request, num, act,  num2):
    if act == 'sum':
        result = f'{num} + {num2} = {num + num2}'
    elif act == 'sub':
        result = f'{num} - {num2} = {num - num2}'
    elif act == 'multi':
        result = f'{num} * {num2} = {num * num2}'
    elif act == 'div':
        try:
            result = f'{num} / {num2} = {num / num2}'
        except ZeroDivisionError:
            result = None

    return render(request, 'calc.html',  {'res': result})
