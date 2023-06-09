# Generated by Django 3.2 on 2023-04-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=300)),
                ('apellidos', models.CharField(max_length=300)),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('f_nacimiento', models.DateField()),
                ('f_publicacion', models.DateField()),
            ],
        ),
    ]
