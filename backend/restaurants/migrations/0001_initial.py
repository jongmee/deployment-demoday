# Generated by Django 3.0.14 on 2022-11-23 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationCategory',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCategory',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=500)),
                ('explain', models.CharField(max_length=500)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('store_image', models.ImageField(null=True, upload_to='media/restaurant')),
                ('location_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.LocationCategory')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.TypeCategory')),
            ],
        ),
    ]
