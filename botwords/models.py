from django.db import models

class BotWords(models.Model):
    botwords_ru = models.TextField()
    botwords_kg = models.TextField()

    @classmethod
    def get_botwords_by_id(cls, botwords_id):
        try:
            return cls.objects.get(id=botwords_id)
        except cls.DoesNotExist:
            return None
