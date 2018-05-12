from django.conf.urls import url
from .views import *

app_name = 'maps'

urlpatterns = [
	url(r'^map$', Map.as_view(), name='map'),
	url(r'^crops$', Crops.as_view(), name='crops'),
	url(r'^irrigation$', Irrigations.as_view(), name='irrigation'),
	url(r'^support$', Support.as_view(), name='support'),
	url(r'^create_measurement$', Create_measurement.as_view(), name='create_measurement'),
	url(r'^$', Measurement.as_view(), name='measurement'),
	url(r'^massive_upload$', Massive_upload.as_view(), name='massive_upload'),
	url(r'^grounds$', Grounds.as_view(), name='ground'),
]
