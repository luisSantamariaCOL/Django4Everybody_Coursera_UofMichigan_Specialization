"""polls URL configuration

Defines the 'urlpatterns' that will be included in mysite.urls.urlpatterns
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]