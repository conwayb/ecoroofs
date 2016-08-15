from django.conf import settings
from django.conf.urls import include, url

from arcutils import admin
from arcutils.drf.routers import DefaultRouter
import arcutils.cas.urls

from . import views
from .locations.views import LocationViewSet


urlpatterns = [
    # Home
    url(r'^$', views.JSAppView.as_view(template_name=settings.HOME_PAGE_TEMPLATE), name='home'),
    url(r'^admin$', views.JSAppView.as_view(template_name='admin.html')),

    # Admin
    url(r'^django-admin/', admin.cas_site.urls),

    # Auth
    url(r'', include(arcutils.cas.urls)),
]

router = DefaultRouter()
urlpatterns += router.urls
