"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # List of all runners
    url(r'^runners/$', views.runners, name='runners'),
    # Individual runner page
    url(r'^runners/(?P<runner_id>\d+)/$', views.runner, name='runner'),
]
