# My Bin Collector

thisghioa;hrgofgn

## Endpoints

sdgfsdfgsdfg

| Method        | URL           | Description  |
| ------------- |:-------------:| -----:|
| GET      | /something     | This gets data |
| POST     | /centered      | This posts data |


## Code example


The below code example demonstrates the APIs URLS associated with there developed resources used as part of the
infrastructure to communicate to the data layer. If the API concept were to be expanded, please ensure the developed
resource names are added to the v1_api.register object which will be access as part of the api/ Url.


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