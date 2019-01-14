from tastypie.resources import ModelResource
from tastypie import fields, utils
from tastypie.authorization import Authorization
from scheduleapi.models import CouncilRegistration, BinSchedule, BinType


class CouncilRegistrationResource(ModelResource):
    class Meta:
        queryset = CouncilRegistration.objects.all()
        resource_name = 'councilregistration'
        fields = ['council_name']
        authorization = Authorization()


class BinTypeResource(ModelResource):
    class Meta:
        queryset = BinType.objects.all()
        resource_name = 'bintype'
        fields = ['bin_type']
        authorization = Authorization()


class BinScheduleResource(ModelResource):
    council_name = fields.ToOneField(CouncilRegistrationResource, attribute='council_id', null=True, full=True)
    bin_type = fields.ToOneField(BinTypeResource, attribute='bin_id', null=True, full=True)
# Performance boost factors adding select_related on FK columns resulting in a single complex query but means later
# use of FK relationships not requiring DB queries

    class Meta:
        queryset = BinSchedule.objects.all().select_related("council_id").select_related("bin_id")
        resource_name = 'binschedule'
        authorization = Authorization()
