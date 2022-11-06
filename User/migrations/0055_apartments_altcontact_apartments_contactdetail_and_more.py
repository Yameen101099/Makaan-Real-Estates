# Generated by Django 4.1.1 on 2022-10-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0054_contactseller'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartments',
            name='altcontact',
            field=models.CharField(default='8778986745', max_length=50),
        ),
        migrations.AddField(
            model_name='apartments',
            name='contactdetail',
            field=models.CharField(default='7698679876', max_length=50),
        ),
        migrations.AddField(
            model_name='apartments',
            name='facing',
            field=models.CharField(default='East', max_length=50),
        ),
        migrations.AddField(
            model_name='apartments',
            name='locality',
            field=models.CharField(default='Kumbha Marg', max_length=50),
        ),
        migrations.AddField(
            model_name='apartments',
            name='roadwidth',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='apartments',
            name='saletype',
            field=models.CharField(default='Fresh', max_length=50),
        ),
        migrations.AddField(
            model_name='apartments',
            name='youare',
            field=models.CharField(default='Agent', max_length=50),
        ),
        migrations.AddField(
            model_name='building',
            name='altcontact',
            field=models.CharField(default='8778986745', max_length=50),
        ),
        migrations.AddField(
            model_name='building',
            name='contactdetail',
            field=models.CharField(default='7698679876', max_length=50),
        ),
        migrations.AddField(
            model_name='building',
            name='facing',
            field=models.CharField(default='East', max_length=50),
        ),
        migrations.AddField(
            model_name='building',
            name='locality',
            field=models.CharField(default='Kumbha Marg', max_length=50),
        ),
        migrations.AddField(
            model_name='building',
            name='roadwidth',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='building',
            name='saletype',
            field=models.CharField(default='Fresh', max_length=50),
        ),
        migrations.AddField(
            model_name='building',
            name='youare',
            field=models.CharField(default='Agent', max_length=50),
        ),
        migrations.AddField(
            model_name='garage',
            name='altcontact',
            field=models.CharField(default='8778986745', max_length=50),
        ),
        migrations.AddField(
            model_name='garage',
            name='contactdetail',
            field=models.CharField(default='7698679876', max_length=50),
        ),
        migrations.AddField(
            model_name='garage',
            name='facing',
            field=models.CharField(default='East', max_length=50),
        ),
        migrations.AddField(
            model_name='garage',
            name='locality',
            field=models.CharField(default='Kumbha Marg', max_length=50),
        ),
        migrations.AddField(
            model_name='garage',
            name='roadwidth',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='garage',
            name='saletype',
            field=models.CharField(default='Fresh', max_length=50),
        ),
        migrations.AddField(
            model_name='garage',
            name='youare',
            field=models.CharField(default='Agent', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='altcontact',
            field=models.CharField(default='8778986745', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='contactdetail',
            field=models.CharField(default='7698679876', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='facing',
            field=models.CharField(default='East', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='locality',
            field=models.CharField(default='Kumbha Marg', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='roadwidth',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='house',
            name='saletype',
            field=models.CharField(default='Fresh', max_length=50),
        ),
        migrations.AddField(
            model_name='house',
            name='youare',
            field=models.CharField(default='Agent', max_length=50),
        ),
        migrations.AddField(
            model_name='office',
            name='altcontact',
            field=models.CharField(default='8778986745', max_length=50),
        ),
        migrations.AddField(
            model_name='office',
            name='contactdetail',
            field=models.CharField(default='7698679876', max_length=50),
        ),
        migrations.AddField(
            model_name='office',
            name='facing',
            field=models.CharField(default='East', max_length=50),
        ),
        migrations.AddField(
            model_name='office',
            name='locality',
            field=models.CharField(default='Kumbha Marg', max_length=50),
        ),
        migrations.AddField(
            model_name='office',
            name='roadwidth',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='office',
            name='saletype',
            field=models.CharField(default='Fresh', max_length=50),
        ),
        migrations.AddField(
            model_name='office',
            name='youare',
            field=models.CharField(default='Agent', max_length=50),
        ),
        migrations.AddField(
            model_name='shop',
            name='altcontact',
            field=models.CharField(default='8778986745', max_length=50),
        ),
        migrations.AddField(
            model_name='shop',
            name='contactdetail',
            field=models.CharField(default='7698679876', max_length=50),
        ),
        migrations.AddField(
            model_name='shop',
            name='facing',
            field=models.CharField(default='East', max_length=50),
        ),
        migrations.AddField(
            model_name='shop',
            name='locality',
            field=models.CharField(default='Kumbha Marg', max_length=50),
        ),
        migrations.AddField(
            model_name='shop',
            name='roadwidth',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='shop',
            name='saletype',
            field=models.CharField(default='Fresh', max_length=50),
        ),
        migrations.AddField(
            model_name='shop',
            name='youare',
            field=models.CharField(default='Agent', max_length=50),
        ),
        migrations.AddField(
            model_name='townhouse',
            name='altcontact',
            field=models.CharField(default='8778986745', max_length=50),
        ),
        migrations.AddField(
            model_name='townhouse',
            name='contactdetail',
            field=models.CharField(default='7698679876', max_length=50),
        ),
        migrations.AddField(
            model_name='townhouse',
            name='facing',
            field=models.CharField(default='East', max_length=50),
        ),
        migrations.AddField(
            model_name='townhouse',
            name='locality',
            field=models.CharField(default='Kumbha Marg', max_length=50),
        ),
        migrations.AddField(
            model_name='townhouse',
            name='roadwidth',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='townhouse',
            name='saletype',
            field=models.CharField(default='Fresh', max_length=50),
        ),
        migrations.AddField(
            model_name='townhouse',
            name='youare',
            field=models.CharField(default='Agent', max_length=50),
        ),
        migrations.AddField(
            model_name='villas',
            name='altcontact',
            field=models.CharField(default='8778986745', max_length=50),
        ),
        migrations.AddField(
            model_name='villas',
            name='contactdetail',
            field=models.CharField(default='7698679876', max_length=50),
        ),
        migrations.AddField(
            model_name='villas',
            name='facing',
            field=models.CharField(default='East', max_length=50),
        ),
        migrations.AddField(
            model_name='villas',
            name='locality',
            field=models.CharField(default='Kumbha Marg', max_length=50),
        ),
        migrations.AddField(
            model_name='villas',
            name='roadwidth',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='villas',
            name='saletype',
            field=models.CharField(default='Fresh', max_length=50),
        ),
        migrations.AddField(
            model_name='villas',
            name='youare',
            field=models.CharField(default='Agent', max_length=50),
        ),
    ]