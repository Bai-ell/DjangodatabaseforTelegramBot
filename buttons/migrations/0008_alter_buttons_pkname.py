# Generated by Django 4.2.7 on 2024-09-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buttons', '0007_alter_buttons_pkname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buttons',
            name='pkname',
            field=models.CharField(choices=[('Back', 'Back'), ('Connect', 'Connect'), ('AreaInfo', 'AreaInfo'), ('Gift', 'Gift'), ('ChoiceMenu', 'ChoiceMenu'), ('ChoiceLang', 'ChoiceLang'), ('Menu', 'Menu'), ('Yes', 'Yes'), ('No', 'No'), ('GoToMenu', 'GoTuMenu'), ('NoAgain', 'NoAgain'), ('Skip', 'Skip')], default='Back', max_length=255, verbose_name='Button Type'),
        ),
    ]
