from django.contrib import admin
from .models import Questionnaire, TypeGift

class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'date_of_birth', 'checked')
    list_filter = ('checked',)
    search_fields = ('name', 'phone_number', 'address')

admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(TypeGift)
