from django.conf.urls import patterns, url

from quizApp import views

urlpatterns = patterns('',
                       url(r'^$', views.get_questions, name='index'),
                       url(r'^(?P<number>\d+)/vote/$', views.vote, name='vote'),


)