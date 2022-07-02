"""polls URL configuration

Defines the 'urlpatterns' that will be included in mysite.urls.urlpatterns
"""

from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path('', views.index, name='index'), # "/polls/"
    path('detail/<int:question_id>', views.detail, name='detail'), # example: "/polls/2"
    path('results/<int:question_id>', views.results, name='results'), # example: "/polls/results/2"
    path('vote/<int:question_id>', views.vote, name='vote'), # example: "/polls/vote/2"
]