# My Bin Collector

## Endpoints

Method | URL | Description
------------ | -------------
Content cell 1 | Content cell 2 | sfg
Content column 1 | Content column 2 | sdfgsdg

```python
#urls.py
v1_api = Api(api_name='v1')
v1_api.register(CouncilRegistrationResource())
v1_api.register(BinScheduleResource())
v1_api.register(BinTypeResource())


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    path('users/', include('users.urls')),
    url(r'^bincollections/', include('scheduleapi.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
```