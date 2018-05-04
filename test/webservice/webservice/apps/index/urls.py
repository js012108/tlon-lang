from django.conf.urls import url
from .views import *

app_name = 'index'

urlpatterns = [
	url(r'^$', Login.as_view(), name='login'),
	url(r'^menu$', Index.as_view(), name='menu'),
]
