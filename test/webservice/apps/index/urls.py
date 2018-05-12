from django.conf.urls import url
from .views import *

app_name = 'index'

urlpatterns = [
	url(r'^$', Index.as_view(), name='menu'),
]
