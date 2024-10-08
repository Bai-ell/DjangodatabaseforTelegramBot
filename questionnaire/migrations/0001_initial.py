# Generated by Django 4.2.7 on 2024-08-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_of_birth', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('type_gift', models.CharField(default='non', max_length=255)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeGift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_type_ru', models.CharField(default='non', max_length=255)),
                ('gift_type_kg', models.CharField(default='non', max_length=255)),
            ],
        ),
    ]
