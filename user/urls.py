from django.urls import path

from .views import name_list
from .views import pet
from .views import calculator
urlpatterns = [
    path('', name_list),
    path('people', name_list),
    path('<int:id>', pet, name='pet'),
    path('calc/<int:num>/<str:act>/<int:num2>', calculator, name='calc')
    ]
