from django.contrib import admin
from .models import CouncilRegistration, BinType, BinSchedule

# Register your models here.

admin.site.register(CouncilRegistration)
admin.site.register(BinSchedule)
admin.site.register(BinType)