"""polls URL configuration

Defines the 'urlpatterns' that will be included in mysite.urls.urlpatterns
"""

from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # "/polls/"
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'), # example: "/polls/2"
    path('results/<int:pk>', views.ResultView.as_view(), name='results'), # example: "/polls/results/2"
    path('vote/<int:question_id>', views.vote, name='vote'), # example: "/polls/vote/2"
]