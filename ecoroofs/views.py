from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from arcutils.settings import get_setting


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

    def get(self, request):
        user = request.user
        return Response({
            'APP': {
                'key': self.app_key,
                'element_name': self.element_name,
                'bundle_path': self.bundle_path,
                'cdn_urls': {
                    'css': [],
                    'js': self.cdn_urls_js,
                },
                'css_path': self.css_path,

                # Config that's passed through to the Angular app.
                'app_config': {
                    'env': settings.ENV,
                    'elementSelector': self.element_name,
                    'baseURL': staticfiles_storage.url(''),
                    'user': {
                        'username': user.username,
                        'full_name': user.get_full_name() if not user.is_anonymous() else None,
                        'is_staff': user.is_staff,
                        'is_superuser': user.is_superuser,
                    },
                },
            },
        })
