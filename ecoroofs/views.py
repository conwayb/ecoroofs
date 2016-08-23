from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from arcutils.settings import get_setting

from .serializers import ModelSerializer


class ModelViewSet(viewsets.ModelViewSet):

    lookup_field = 'slug'
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    @classmethod
    def from_model(cls, model, **cls_attrs):
        # Returns a subclass configured with the specified model.
        cls_attrs.setdefault('queryset', model.objects.all())
        cls_attrs.setdefault('serializer_class', ModelSerializer.from_model(model))
        return type(cls.__name__, (cls,), cls_attrs)


class AppView(APIView):

    app_key = settings.HOME_PAGE_APP_KEY
    renderer_classes = [TemplateHTMLRenderer]

    @property
    def bundle_path(self):
        return 'bundles/{self.app_key}.bundle.js'.format(self=self)

    @property
    def css_path(self):
        return '{self.app_key}/main.css'.format(self=self)

    @property
    def cdn_urls_css(self):
        setting = 'APPS.{self.app_key}.cdn_urls.css'.format(self=self)
        return get_setting(setting, [])

    @property
    def cdn_urls_js(self):
        setting = 'APPS.{self.app_key}.cdn_urls.js'.format(self=self)
        return get_setting(setting, [])

    @property
    def element_name(self):
        # E.g., "ecoroofs-map"
        return '{settings.PACKAGE}-{self.app_key}'.format(settings=settings, self=self)

    @property
    def template_name(self):
        return '{self.app_key}.html'.format(self=self)

    @property
    def js_app_context(self):
        user = self.request.user
        return {
            'key': self.app_key,
            'element_name': self.element_name,
            'bundle_path': self.bundle_path,
            'cdn_urls': {
                'css': [],
                'js': self.cdn_urls_js,
            },
            'css_path': self.css_path,

            # Config that's passed through to the JavaScript app.
            'app_config': {
                'env': settings.ENV,
                'elementSelector': self.element_name,
                'baseURL': staticfiles_storage.url(''),
                'user': {
                    'username': user.username,
                    'fullName': user.get_full_name() if not user.is_anonymous() else None,
                    'isStaff': user.is_staff,
                    'isSuperuser': user.is_superuser,
                },
                'map': settings.MAP,
            },
        }

    def get(self, request):
        return Response({
            'APP': self.js_app_context,
        })
