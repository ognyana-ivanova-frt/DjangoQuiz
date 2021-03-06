from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quizApp/', include('quizApp.urls',  namespace="quizApp")),
    (r'^settings/', include('dbsettings.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )