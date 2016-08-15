from django.db import models
from django.contrib.gis.db.models import PointField

from ..models import SlugFieldMixin


class Location(SlugFieldMixin):

    name = models.CharField(max_length=255, unique=True)
    point = PointField()

    def __str__(self):
        return '{self.name} at {self.point.y}, {self.point.x}'.format_map(locals())
