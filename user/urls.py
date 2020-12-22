from django.urls import path

from .views import name_list
from .vievsPet import pet
urlpatterns = [
    path('', name_list),
    path('people', name_list),
    path('dogs', pet)
    ]
