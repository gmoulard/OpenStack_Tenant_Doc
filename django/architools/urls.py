# -*- coding: utf-8 -*-
"""

@author: GAYM6331
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

