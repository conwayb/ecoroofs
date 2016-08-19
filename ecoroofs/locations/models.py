from django.db import models
from django.contrib.gis.db.models import PointField

from ..models import BaseModel


__all__ = [
    'Location',
    'Watershed',
]


class Location(BaseModel):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255, unique=True)
    point = PointField()
    watershed = models.ForeignKey('Watershed', null=True, blank=True)

    def __str__(self):
        return '{self.name} at {self.point.y}, {self.point.x}'.format_map(locals())


class Watershed(BaseModel):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
