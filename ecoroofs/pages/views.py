from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

from ..views import AppView
from .models import Page
from .serializers import PageSerializer


class IsPublished(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.published:
            return True
        user = request.user
        return user and user.is_authenticated() and (user.is_staff or user.is_superuser)


class PageView(RetrieveAPIView, AppView):

    app_key = 'pages'
    lookup_field = 'slug'
    permission_classes = [IsPublished]
    queryset = Page.objects.filter(published=True)
    serializer_class = PageSerializer
    template_name = 'pages/default.html'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['APP'] = self.js_app_context
        return Response(data)


page_view = PageView.as_view()
