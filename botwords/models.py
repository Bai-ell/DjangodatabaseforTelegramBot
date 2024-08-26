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

    botwords_ru = models.TextField()
    botwords_kg = models.TextField()
    pkwords = models.CharField(max_length=255, choices=PkNames.choices, default=PkNames.GREETINGS)

    @classmethod
    def get_botwords_by_id(cls, botwords_id):
        try:
            return cls.objects.get(id=botwords_id)
        except cls.DoesNotExist:
            return None