from django.shortcuts import render, HttpResponse, redirect
from scheduleapi.models import PostcodeTBL, PostcodeGrouping, BinScheduleMapping
# Create your views here.
# function based view or class based views


# functional based view
def home(request):
    if request.user.is_authenticated:
        postcode = request.user.postcode
        grouping_id = PostcodeTBL.objects.filter(postcode=postcode)

        postcode_id = 0
        for item in grouping_id:
            postcode_id = item.postcode_id

        grouping_row = PostcodeGrouping.objects.filter(group_id=postcode_id)
        postcode_grouping_id = 0
        for grouping_item in grouping_row:
            postcode_grouping_id = grouping_item.grouping_id

        bs_mapping_table_row = BinScheduleMapping.objects.filter(postcodegrouping_id=postcode_grouping_id)

        bin_schedule_list = []
        for bs_mapping_table_item in bs_mapping_table_row:
            bin_schedule_list.append(bs_mapping_table_item.binschedule_id)

        dates = []
        bins = []

        for bin_schedule_item in bin_schedule_list:
            dates.append(bin_schedule_item.date)
            bins.append(bin_schedule_item.bin_id)

        return render(
            request,
            'bincollections/index.html',
            {
                'date1': dates[0], 'bin1': bins[0],
                'date2': dates[1], 'bin2': bins[1],
                'date3': dates[2], 'bin3': bins[2]
            }
        )
    else:
        return redirect('login')


def settings(request):
    return render(request, 'settings.html')
