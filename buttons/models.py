from django.db import models



class Buttons(models.Model):
    class PkNames(models.TextChoices):
        BACK = 'Back', 'Back'
        CONNECT = 'Connect', 'Connect'
        AREAINFO = 'AreaInfo', 'AreaInfo'
        GIFT = 'Gift', 'Gift'
        CHOICEMENU = 'ChoiceMenu', 'ChoiceMenu'
        CHOICELANG = 'ChoiceLang', 'ChoiceLang'
        MENU = 'Menu', 'Menu'
        YES = 'Yes', 'yes'
        NO = 'No', 'no'

    button_kg = models.CharField(max_length=255)
    button_ru = models.CharField(max_length=255)
    pkname = models.CharField(max_length=255, choices=PkNames.choices, default=PkNames.BACK)

    @classmethod
    def get_button_by_id(cls, button_id):
        try:
            return cls.objects.get(id=button_id)
        except cls.DoesNotExist:
            return None