import logging

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.gis.db.models import PointField

from ..models import BaseModel
from ..neighborhoods.models import Neighborhood


__all__ = [
    'Location',
    'Watershed',
]


log = logging.getLogger(__name__)


class Location(BaseModel):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255, unique=True)
    point = PointField()
    neighborhood = models.ForeignKey('neighborhoods.Neighborhood', null=True, editable=False)
    watershed = models.ForeignKey('Watershed', null=True, blank=True)

    def set_neighborhood_automatically(self):
        """Set neighborhood via spatial contains query.

        Finds the neighborhood (or neighborhoods) this Location is
        contained in. If it's in multiple neighborhoods, the first one
        returned from the database (ordered by name) will be used.

        """
        q = Neighborhood.objects.filter(geom__contains=self.point)
        neighborhood = q.first()
        if q.count() > 1:
            neighborhoods = q.all()
            log.warn('Location "%s" is in multiple neighborhoods: %s', self, neighborhoods)
        self.neighborhood = neighborhood

    def __str__(self):
        return '{self.name} at {self.point.y}, {self.point.x}'.format_map(locals())


@receiver(pre_save, sender=Location)
def set_neighborhood(sender, instance: Location, **kwargs):
    instance.set_neighborhood_automatically()


class Watershed(BaseModel):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
