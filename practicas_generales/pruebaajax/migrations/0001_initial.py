# Generated by Django 4.2.2 on 2023-06-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgregarMateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=50, verbose_name='Materia')),
                ('creditos', models.IntegerField(max_length=2, verbose_name='creditos')),
            ],
        ),
    ]