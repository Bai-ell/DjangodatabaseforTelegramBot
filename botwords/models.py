from django.db import models

class BotWords(models.Model):
    class PkNames(models.TextChoices):
        GREETINGS  = 'Greetings', 'greetings'
        CHANGELANG = 'ChangeLang', 'changelang'
        INFOOCTOBERAREA  = 'InfoOctoberArea', 'infooctoberarea'
        MTB = 'Mtb', 'mtb'
        MED = 'Med', 'med'
        OOU = 'OOU', 'oou'
        CONNECT = 'Connect', 'connect'
        LINKS = 'Links', 'links'
        CONTACTS = 'Contacts', 'contacts'
        CHOICE = 'Choice', 'choice'
        GOTOMENU = 'GoToMenu', 'gotomenu'
        CHOICEGIFT = 'ChoiceGift', 'choicegift'
        QUESTIONNAIRE = 'Questionnaire', 'questionnaire'
        STARTQUESTIONNAIRE  = 'StartQuestionnaire', 'startquestionnaire'
        CHOICEGIFTQUESTIONNAIRE = 'ChoiceGiftQuestionnaire', 'choicegiftquestionnaire'
        ANSWERNAME =  'AnswerName', 'answername'
        ANSWERPHONENUMBER = 'AnswerPhoneNumber', 'answerphonenumber'
        ANSWERDATEOFBIRTH = 'AnswerDateOfBirth', 'answerdateofbirth'
        ANSWERADRESS = 'AnswerAdress', 'answeradreass'
        ENDQUESTIONNAIRE = 'EndQuestionnaire', 'endquestionnaire'
        GIFT = 'Gift', 'gift'
        NAME = 'Name', 'name'
        PHONE = 'Phone', 'phone'
        BIRTHDATE = 'BirthDate', 'birthdate'
        ADDRESS = 'Address', 'address'
        SENDQUESTIONNAIRE = 'SendQuestionnaire', 'sendquestionnaire'
        WARNINGWORD = 'WarningWord', 'warningword'
        DATASEND = 'DataSend', 'datasend'
        CORRECTNUMBER  = 'CorrectNumber', 'correctnumber'
        CORRECTDATE = 'CorrectDate', 'correctdate'
        ADDITIONALREQUEST= 'AdditionalInfoRequest', 'additionalrequest'
        ADDITONALTEXT = 'AdditionalText', 'additionaltext'
        



    botwords_ru = models.TextField()
    botwords_kg = models.TextField()
    pkwords = models.CharField(max_length=255, choices=PkNames.choices, default=PkNames.GREETINGS)

    @classmethod
    def get_botwords_by_id(cls, botwords_id):
        try:
            return cls.objects.get(id=botwords_id)
        except cls.DoesNotExist:
            return None