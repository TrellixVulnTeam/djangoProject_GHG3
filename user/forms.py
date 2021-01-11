from django import forms
from .models import UsersModel
from .models import PetsModel


class UserModel(forms.ModelForm):
    class Meta:
        model=UsersModel
        fields = ('name', 'age')

class PetModel(forms.ModelForm):
    class Meta:
        model=PetsModel
        fields = ('name', 'kind', 'age', 'ovner')