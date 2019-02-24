from django.contrib import admin
from django.conf.urls import url
from .views import Homeview, get_data, ChartData

urlpatterns = [
    # url(r'^$', Homeview.as_view(), name='home'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view(), name='chart-data'),


]
