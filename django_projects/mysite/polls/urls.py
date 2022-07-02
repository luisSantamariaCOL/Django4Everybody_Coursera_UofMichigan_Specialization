"""polls URL configuration

Defines the 'urlpatterns' that will be included in mysite.urls.urlpatterns
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # "/polls/"
    path('<int:question_id>', views.detail, name='detail'), # example: "/polls/detail/2"
    path('results/<int:question_id>', views.results, name='results'), # example: "/polls/results/2"
    path('vote/<int:question_id>', views.vote, name='vote'), # example: "/polls/votes/2"
]