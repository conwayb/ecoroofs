from django.db.models import Sum

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..views import ModelViewSet
from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(ModelViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer


@api_view()
def square_footage(request, neighborhood=None):
    """Get location square footage.

    The total square footage of all locations is always included. If
    a neighborhood is specified, the neighborhood total will be included
    too. The structure of JSON responses is::

        {
            "total": N,
            "neighborhood": "{neighborhood}"|null,
            "neighborhood_total": N|null
        }

    """
    q = Location.objects.all()
    total = q.aggregate(total=Sum('square_footage'))['total']

    if neighborhood:
        q = q.filter(neighborhood__slug=neighborhood)
        neighborhood_total = q.aggregate(total=Sum('square_footage'))['total']
    else:
        neighborhood_total = None

    return Response({
        'total': total,
        'neighborhood': neighborhood,
        'neighborhood_total': neighborhood_total,
    })
