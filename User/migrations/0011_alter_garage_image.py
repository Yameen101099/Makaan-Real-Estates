# Generated by Django 4.1.1 on 2022-10-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_garage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garage',
            name='image',
            field=models.FileField(upload_to='images/Garage'),
        ),
    ]
