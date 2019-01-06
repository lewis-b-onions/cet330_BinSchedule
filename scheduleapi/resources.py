from tastypie.resources import ModelResource
from tastypie import fields, utils
from scheduleapi.models import CouncilRegistration, BinSchedule

class CouncilRegistrationResource(ModelResource):

	class Meta:
		queryset = CouncilRegistration.objects.all()
		resource_name = 'councilregistration'


class BinScheduleResource(ModelResource):
    # fk = fields.ForeignKey(CouncilRegistrationResource, attribute='council_id', full=True)
    fk = fields.ToOneField(CouncilRegistrationResource, attribute='council_id', null=True, full=True)
    class Meta:
        queryset = BinSchedule.objects.all()
        resource_name = 'binschedule'

