# Generated by Django 4.2.7 on 2024-09-06 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botwords', '0011_alter_botwords_pkwords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botwords',
            name='botwords_kg',
            field=models.TextField(verbose_name='Kyrgyz Text'),
        ),
        migrations.AlterField(
            model_name='botwords',
            name='botwords_ru',
            field=models.TextField(verbose_name='Russian Text'),
        ),
        migrations.AlterField(
            model_name='botwords',
            name='pkwords',
            field=models.CharField(choices=[('Greetings', 'Greetings'), ('ChangeLang', 'ChangeLang'), ('InfoOctoberArea', 'InfoOctoberArea'), ('Mtb', 'Mtb'), ('Med', 'Med'), ('OOU', 'OOU'), ('Connect', 'Connect'), ('Links', 'Links'), ('Contacts', 'Contacts'), ('Choice', 'Choice'), ('GoToMenu', 'GoToMenu'), ('ChoiceGift', 'ChoiceGift'), ('Questionnaire', 'Questionnaire'), ('StartQuestionnaire', 'StartQuestionnaire'), ('ChoiceGiftQuestionnaire', 'ChoiceGiftQuestionnaire'), ('AnswerName', 'AnswerName'), ('AnswerPhoneNumber', 'AnswerPhoneNumber'), ('AnswerDateOfBirth', 'AnswerDateOfBirth'), ('AnswerAdress', 'AnswerAdress'), ('EndQuestionnaire', 'EndQuestionnaire'), ('Gift', 'Gift'), ('Name', 'Name'), ('Phone', 'Phone'), ('BirthDate', 'BirthDate'), ('Address', 'Address'), ('SendQuestionnaire', 'SendQuestionnaire'), ('WarningWord', 'WarningWord'), ('DataSend', 'DataSend'), ('CorrectNumber', 'CorrectNumber'), ('CorrectDate', 'CorrectDate'), ('AdditionalInfoRequest', 'AdditionalInfoRequest'), ('AdditionalText', 'AdditionalText')], default='Greetings', max_length=255, verbose_name='Keyword'),
        ),
    ]
