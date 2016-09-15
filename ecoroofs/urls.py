from django.conf.urls import include, url

from rest_framework import serializers

from arcutils import admin
from arcutils.drf.routers import DefaultRouter
import arcutils.cas.urls

from .serializers import ModelSerializer
from .views import AppView, ModelViewSet

from .locations.models import Location
from .locations.views import square_footage

from .pages.models import Page


urlpatterns = [
    # Home
    url(r'^$', AppView.as_view(template_name='base.html'), name='home'),

    # Admin
    url(r'^admin/', admin.cas_site.urls),

    # Auth
    url(r'', include(arcutils.cas.urls)),

    # API
    url(r'^_/locations/square-footage$', square_footage, name='square-footage'),
    url(r'^_/locations/square-footage/(?P<neighborhood>.+)$', square_footage,
        name='square-footage-neighborhood'),
]


router = DefaultRouter()
router.register(r'_/locations', ModelViewSet.from_model(Location))
router.register(r'_/pages', ModelViewSet.from_model(
    Page,
    queryset=Page.objects.filter(published=True),
    serializer_class=ModelSerializer.from_model(Page, path=serializers.CharField()),
))
urlpatterns += router.urls
