from django.conf.urls import include, url
from django.contrib import admin

import arcutils.cas.urls

from . import views


urlpatterns = [
    # Home
    url(r'^$', views.home),

    # Admin
    url(r'^admin/', admin.site.urls),

    # Auth
    url(r'', include(arcutils.cas.urls)),
]
