from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions


from .models import Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location


class LocationViewSet(viewsets.ModelViewSet):

    permission_classes = [DjangoModelPermissions]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
