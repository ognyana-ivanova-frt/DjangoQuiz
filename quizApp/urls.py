from django.conf.urls import patterns, url
from quizApp import views

"""
URL scheme
"""

urlpatterns = patterns('',
       # /quizApp/
       url(r'^$', views.get_questions, name='index'),
       # /quizApp/2/vote
       url(r'^(?P<number>\d+)/vote/$', views.vote, name='vote'),
)