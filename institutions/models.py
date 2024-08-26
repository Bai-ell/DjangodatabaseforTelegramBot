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
        


class ShortNamesMta(models.Model):
    string_ru = models.TextField()
    string_kg = models.TextField()

    @classmethod
    def get_short_mta_by_id(cls, short_mta_id):
        try:
            return cls.objects.get(id=short_mta_id)
        except cls.DoesNotExist:
            return None


class Institution(models.Model):
    string_ru = models.TextField()
    string_kg = models.TextField()

    @classmethod
    def get_med_institution_by_id(cls, institution_id):
        try:
            return cls.objects.get(id=institution_id)
        except cls.DoesNotExist:
            return None
