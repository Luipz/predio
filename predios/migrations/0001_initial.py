# Generated by Django 3.2.9 on 2021-11-13 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='predio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('car_brand', models.CharField(max_length=100)),
                ('license_plate', models.CharField(max_length=100)),
                ('usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predios', to='predios.usuarios')),
            ],
        ),
    ]