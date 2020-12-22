from django.contrib import admin

from .models import UsersModel
from .models import PetsModel
# Register your models here.
admin.site.register(UsersModel)
admin.site.register(PetsModel)