from django.contrib import admin
from .models import Mta, Institution, ShortNamesMta


admin.site.register(Institution)
admin.site.register(Mta)
admin.site.register(ShortNamesMta)
