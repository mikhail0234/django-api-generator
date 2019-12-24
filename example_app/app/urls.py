from django.conf.urls import include, url
try:
  from django.conf.urls import patterns
except ImportError:
  pass
import django
from django.contrib import admin
from app import views


urlpatterns = [

url(r'^product/(?P<id>[0-9]+)$', views.ProductAPIView.as_view()),
url(r'^product/$', views.ProductAPIListView.as_view()),

]
