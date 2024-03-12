# Generated by Django 5.0.3 on 2024-03-10 14:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IC', 'Ice-Creams'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('CZ', 'Cheese'), ('CR', 'Curd'), ('ML', 'Milk'), ('PN', 'Paneer'), ('GH', 'Ghee')], max_length=2),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Barisal', 'Barisal'), ('Sylhet', 'Sylhet'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh'), ('Jessore', 'Jessore'), ('Comilla', 'Comilla')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
