from django.contrib import admin
from .models import CouncilRegistration, BinType, BinSchedule, PostcodeTBL, PostcodeGrouping, BinScheduleMapping, UserBinMap

# Register your models here.

admin.site.register(CouncilRegistration)
admin.site.register(BinSchedule)
admin.site.register(BinType)
admin.site.register(PostcodeTBL)
admin.site.register(PostcodeGrouping)
admin.site.register(BinScheduleMapping)
admin.site.register(UserBinMap)