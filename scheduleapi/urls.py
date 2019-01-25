from django.conf.urls import url
from . import views
# . import views will look in any folder for a views file - Reference other views in other apps

""" All the URLs that are going to be handled by the scheduleapi app"""

urlpatterns = [
# Start ^ and Stop $ - urls in project file will look into this for page loc e.g. bincollections
    url(r'^$', views.home, name='homepage'),
    url('settings/', views.settings, name='settings'),

]