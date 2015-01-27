from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from scaler import views

router = routers.DefaultRouter()
router.register(r'compounds', views.CompoundsViewSet)
router.register(r'foods', views.CompoundsFoodsViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
)
