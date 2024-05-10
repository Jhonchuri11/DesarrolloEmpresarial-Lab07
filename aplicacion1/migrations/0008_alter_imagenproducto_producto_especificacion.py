# Generated by Django 4.2.5 on 2023-10-04 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0007_rename_imagenproductos_imagenproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='aplicacion1.producto'),
        ),
        migrations.CreateModel(
            name='especificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=100)),
                ('marcas', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('linea', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('accesorio', models.CharField(max_length=100)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion1.producto')),
            ],
        ),
    ]