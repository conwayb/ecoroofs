from ..views import ModelViewSet
from .models import Page
from .serializers import PageSerializer


class PageViewSet(ModelViewSet):

    queryset = Page.objects.filter(published=True)
    serializer_class = PageSerializer
