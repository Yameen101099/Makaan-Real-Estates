# Generated by Django 4.1.1 on 2022-10-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0044_office_additionalroom_office_tokenamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='cornerprop',
            field=models.CharField(default='NO', max_length=5),
        ),
    ]