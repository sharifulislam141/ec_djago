# Generated by Django 5.0.3 on 2024-03-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_delete_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CZ', 'Cheese'), ('CR', 'Curd'), ('PN', 'Paneer'), ('MS', 'Milkshake'), ('GH', 'Ghee'), ('IC', 'Ice-Creams'), ('LS', 'Lassi'), ('ML', 'Milk')], max_length=2),
        ),
    ]
