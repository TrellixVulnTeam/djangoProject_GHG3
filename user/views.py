from django.shortcuts import render
from .models import UsersModel


# Create your views here.

def name_list(request):
    qs = UsersModel.objects.all()

    return render(request, 'user.html', {'names_list': qs})
