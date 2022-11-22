# Generated by Django 4.1.3 on 2022-11-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_alter_restaurant_location_type_alter_restaurant_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='store_image',
            field=models.ImageField(null=True, upload_to='restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location_type',
            field=models.CharField(choices=[('front_gate', '정문'), ('back_gate', '후문'), ('sinchon', '신촌'), ('south_gate', '남문'), ('daeheung', '대흥')], max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='type',
            field=models.CharField(choices=[('japanese', '일식'), ('western', '양식'), ('chinese', '중식'), ('korean', '한식')], max_length=20),
        ),
    ]