# My Bin Collector

## Endpoints

| Method        | URL           | Description  |
| ------------- |:-------------:| -----:|
| GET      | /something     | This gets data |
| POST     | /centered      | This posts data |

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