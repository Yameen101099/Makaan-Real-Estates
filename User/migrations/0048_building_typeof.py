# Generated by Django 4.1.1 on 2022-10-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0047_alter_building_image1_alter_building_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='typeof',
            field=models.CharField(default='sell', max_length=50),
        ),
    ]
