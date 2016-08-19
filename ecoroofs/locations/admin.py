from arcutils import admin

from ..admin import GeoModelAdmin
from .models import *  # noqa


admin.cas_site.register(Location, GeoModelAdmin)
admin.cas_site.register(Watershed)
