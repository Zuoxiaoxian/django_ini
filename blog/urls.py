from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^time/$', views.tody_is, name='todays_tome'),
]