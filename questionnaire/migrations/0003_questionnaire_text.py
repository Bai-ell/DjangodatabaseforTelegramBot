# Generated by Django 4.2.7 on 2024-09-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_alter_questionnaire_type_gift'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='text',
            field=models.CharField(default='non', max_length=255),
        ),
    ]
