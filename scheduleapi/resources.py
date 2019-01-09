from tastypie.resources import ModelResource
from tastypie import fields, utils
from scheduleapi.models import CouncilRegistration, BinSchedule, BinType


class CouncilRegistrationResource(ModelResource):
    class Meta:
        queryset = CouncilRegistration.objects.all()
        resource_name = 'councilregistration'


class BinTypeResource(ModelResource):
    class Meta:
        queryset = BinType.objects.all()
        resource_name = 'bintype'


class BinScheduleResource(ModelResource):
    # fk = fields.ForeignKey(CouncilRegistrationResource, attribute='council_id', full=True)
    fk = fields.ToOneField(CouncilRegistrationResource, attribute='council_id', null=True, full=True)
    fk1 = fields.ToOneField(BinTypeResource, attribute='bin_id', null=True, full=True)

    class Meta:
        queryset = BinSchedule.objects.all()
        resource_name = 'binschedule'
