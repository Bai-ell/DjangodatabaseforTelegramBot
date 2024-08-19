from django.db import models

class Buttons(models.Model):
    button_kg = models.CharField(max_length=255)
    button_ru = models.CharField(max_length=255)

    @classmethod
    def get_button_by_id(cls, button_id):
        try:
            return cls.objects.get(id=button_id)
        except cls.DoesNotExist:
            return None