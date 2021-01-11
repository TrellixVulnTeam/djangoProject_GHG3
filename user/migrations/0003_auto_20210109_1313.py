# Generated by Django 3.1.4 on 2021-01-09 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201222_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petsmodel',
            options={'verbose_name': 'Список питомцев'},
        ),
        migrations.AlterField(
            model_name='petsmodel',
            name='ovner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ovners', to='user.usersmodel', verbose_name='Хозяин'),
        ),
        migrations.AlterModelTable(
            name='petsmodel',
            table='pet',
        ),
    ]