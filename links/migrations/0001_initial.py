# Generated by Django 4.2.7 on 2024-08-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru_name', models.CharField(max_length=50)),
                ('kg_name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru_name', models.CharField(max_length=50)),
                ('kg_name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
    ]
