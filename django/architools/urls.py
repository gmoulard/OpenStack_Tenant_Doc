# -*- coding: utf-8 -*-
"""

@author: GAYM6331
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # url(r'^(?P<TENANTLIST_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<id>[0-9]+)/results/$', views.results, name='results'),
]

