from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from scaler.views import CompoundsViewSet, CompoundsFoodsViewSet


router = routers.DefaultRouter()
router.register(r'compounds', CompoundsViewSet)
router.register(r'foods', CompoundsFoodsViewSet)

urlpatterns = patterns('',
    url(r'^scaler/', include('scaler.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
)
