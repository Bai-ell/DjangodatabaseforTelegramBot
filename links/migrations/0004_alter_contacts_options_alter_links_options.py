# Generated by Django 4.2.7 on 2024-09-06 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_alter_contacts_kg_name_alter_contacts_link_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='links',
            options={'verbose_name': 'Link', 'verbose_name_plural': 'Links'},
        ),
    ]
