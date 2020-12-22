from django.db import models

# Create your models here.

class UsersModel(models.Model):
    class Meta:
        db_table = 'name_list'
        verbose_name = 'Список людей'
    name = models.CharField(max_length=30, verbose_name='Имя')
    age = models.IntegerField(default=0, verbose_name='Возраст')

    def __str__(self):
        return self.name

class PetsModel(models.Model):
    class Meta:
        db_table = 'pet'
        verbose_name = 'Список питомцев'

    name = models.CharField(max_length=30, verbose_name='Кличка')
    kind = models.CharField(max_length=30, verbose_name='Порода')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    ovner = models.ForeignKey(UsersModel, verbose_name='Хозяин', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

