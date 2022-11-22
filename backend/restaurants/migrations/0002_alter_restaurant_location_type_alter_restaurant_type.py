# Generated by Django 4.1.3 on 2022-11-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='location_type',
            field=models.CharField(choices=[('winter', 'winter'), ('spring', 'spring'), ('summer', 'summer'), ('fall', 'fall')], max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='type',
            field=models.CharField(choices=[('winter', 'winter'), ('spring', 'spring'), ('summer', 'summer'), ('fall', 'fall')], max_length=20),
        ),
    ]