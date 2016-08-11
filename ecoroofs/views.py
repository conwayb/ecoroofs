from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class JSAppView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = settings.HOME_PAGE_TEMPLATE

    def get(self, request):
        user = request.user
        return Response({
            'JS_APP_CONFIG': {
                'baseURL': staticfiles_storage.url(''),
                'user': {
                    'username': user.username,
                    'full_name': user.get_full_name() if not user.is_anonymous() else None,
                    'is_staff': user.is_staff,
                    'is_superuser': user.is_superuser,
                }
            }
        })
