from arcutils import admin

from ..admin import GeoModelAdmin
from .models import Location


admin.cas_site.register(Location, GeoModelAdmin)
