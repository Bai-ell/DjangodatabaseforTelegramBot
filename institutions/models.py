from django.db import models

class Mta(models.Model):
    string_ru = models.TextField()
    string_kg = models.TextField()

    @classmethod
    def get_mta_by_id(cls, mta_id):
        try:
            return cls.objects.get(id=mta_id)
        except cls.DoesNotExist:
            return None
        



class Institution(models.Model):
    class PkInstitutions(models.TextChoices):
        OOU  = 'Oou', 'oou'
        MED = 'Med', 'med'

    string_ru = models.TextField()
    string_kg = models.TextField()
    pkinstitutions = models.CharField(max_length=255, choices=PkInstitutions.choices, default=PkInstitutions.OOU)

    @classmethod
    def get_med_institution_by_id(cls, institution_id):
        try:
            return cls.objects.get(id=institution_id)
        except cls.DoesNotExist:
            return None
