from django.conf import settings
from django.conf.urls import include, url

from arcutils import admin
from arcutils.drf.routers import DefaultRouter
import arcutils.cas.urls

from .locations.models import Location
from .views import AppView, ModelViewSet
from .pages.views import PageView


urlpatterns = [
    # Home
    url(r'^$', AppView.as_view(app_key=settings.HOME_PAGE_APP_KEY), name='home'),
    url(r'^map$', AppView.as_view(app_key='map'), name='map'),

    # Admin
    url(r'^admin/', admin.cas_site.urls),

    # Auth
    url(r'', include(arcutils.cas.urls)),

    # Pages
    url(r'^pages/(?P<slug>.+)', PageView.as_view(), name='page'),
]


router = DefaultRouter()
router.register(r'_/locations', ModelViewSet.from_model(Location))
urlpatterns += router.urls
