from django.db import models

class Questionnaire(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=25)
    address = models.TextField()
    type_gift = models.CharField(max_length=255)  # Поле с значением по умолчанию
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


class TypeGift(models.Model):
    gift_type_ru = models.CharField(max_length=255, default='non')
    gift_type_kg = models.CharField(max_length=255,default='non')
    