from ..serializers import ModelSerializer
from .models import Location


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
