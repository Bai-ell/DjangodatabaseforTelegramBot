from django.db import models

class Questionnaire(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.TextField()
    checked = models.BooleanField(default=False)  # поле для отметки проверки

    def __str__(self):
        return f"{self.name} - {self.phone_number}"
