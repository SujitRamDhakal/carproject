# Generated by Django 4.1.5 on 2023-08-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cars_carimage_alter_cars_cardesc_alter_cars_carname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='carimage',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
