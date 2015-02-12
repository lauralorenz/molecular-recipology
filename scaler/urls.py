from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^', 'scaler.views.index'),
    )