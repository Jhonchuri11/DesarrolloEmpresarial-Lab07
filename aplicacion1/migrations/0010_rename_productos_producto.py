# Generated by Django 4.2.5 on 2023-10-04 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0009_productos_remove_producto_categoria_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]
