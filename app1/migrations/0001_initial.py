# Generated by Django 4.2.6 on 2023-10-25 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_alumno', models.IntegerField()),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('puntaje', models.CharField(max_length=20)),
            ],
        ),
    ]