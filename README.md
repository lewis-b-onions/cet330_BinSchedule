# My Bin Collector

Welcome to the My Bin Collector API documentation which will provide you a high level understanding of the core requirements, Tastpie overview, API endpoints, a code example and various Tastypie help material.

## Requirements

### Core

* Python 2.7+ or Python 3.4+
* Django - 1.11 (LTS), 2.0 (LTS) or 2.1 - the last two LTS and the last incremental release are supported.




## Django Tastypie

There are other API frameworks out there for Django. You need to assess the options available and decide for yourself.
That said, here are some common reasons for tastypie.

* You need an API that is RESTful and uses HTTP well.
* You want to support deep relations.
* You DON'T want to have to write your own serializer to make the output right.
* You want an API framework that has little magic, very flexible and maps well to the problem domain.
* You want/need XML serialization that is treated equally to JSON (and YAML is there too).

## Endpoints

### Application endpoints


| Method        | URL           | Description  | Parameters | API Key
| ------------- |:-------------:| -----:| -----:| -----:|
| GET      | /api/v1/binschedule/    | This gets data | N/A [Filter available, see Tastypie docs] | True
| POST     | /api/v1/binschedule/      | This posts data | [Council name] [date] [bin_type] | True


## Code example


The below code example demonstrates the APIs URLS associated with there developed resources used as part of the
infrastructure to communicate to the data layer. If the API concept were to be expanded, please ensure the developed
resource names are added to the v1_api.register object which will be access as part of the "api/" URL.


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

## Help material

* https://django-tastypie.readthedocs.io/en/latest/
* http://tastypieapi.org/
* https://realpython.com/create-a-super-basic-rest-api-with-django-tastypie/
* https://www.agiliq.com/blog/2015/03/getting-started-with-django-tastypie/
* https://codeburst.io/create-a-django-api-in-under-20-minutes-2a082a60f6f3