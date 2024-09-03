# Generated by Django 4.2.7 on 2024-09-03 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botwords', '0007_alter_botwords_pkwords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botwords',
            name='pkwords',
            field=models.CharField(choices=[('Greetings', 'greetings'), ('ChangeLang', 'changelang'), ('InfoOctoberArea', 'infooctoberarea'), ('Mtb', 'mtb'), ('Med', 'med'), ('OOU', 'oou'), ('Connect', 'connect'), ('Links', 'links'), ('Contacts', 'contacts'), ('Choice', 'choice'), ('GoToMenu', 'gotomenu'), ('ChoiceGift', 'choicegift'), ('Questionnaire', 'questionnaire'), ('StartQuestionnaire', 'startquestionnaire'), ('ChoiceGiftQuestionnaire', 'choicegiftquestionnaire'), ('AnswerName', 'answername'), ('AnswerPhoneNumber', 'answerphonenumber'), ('AnswerDateOfBirth', 'answerdateofbirth'), ('AnswerAdress', 'answeradreass'), ('EndQuestionnaire', 'endquestionnaire'), ('Gift', 'gift'), ('Name', 'name'), ('Phone', 'phone'), ('BirthDate', 'birthdate'), ('Address', 'address'), ('SendQuestionnaire', 'sendquestionnaire'), ('WarningWord', 'warningword'), ('DataSend', 'datasend'), ('CorrectNumber', 'correctnumber'), ('CorrectDate', 'correctdate'), ('AdditionalText', 'additionaltext')], default='Greetings', max_length=255),
        ),
    ]
