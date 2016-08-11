from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.storage import staticfiles_storage

from arcutils.templatetags.arc import cdn_url


register = template.Library()


SYSTEMJS_IMPORT_TEMPLATE = """\
<script>
    System.import('%(app_name)s').catch(function (error) {
        console.error(error);
    });
</script>
"""


@register.simple_tag
def systemjs_block(app_name, *cdn_urls):
    """Output <script> tags for loading a SystemJS entry point.

    This chooses the appropriate scripts according to the ``DEBUG``
    setting. In debug mode, this outputs the following tags::

        <script src="/static/node_modules/core-js/client/shim.min.js"></script>
        <script src="/static/node_modules/systemjs/dist/system.src.js"></script>
        <script src="/static/systemjs.config.js"></script>
        <script>
            System.import('{app_name}').catch(function (err) {
                console.error(err);
            });
        </script>

    In production, this outputs the following tags::

        CDN <script>s
        <script src="/static/{app_name}.bundle.js"></script>

    .. note:: These examples assume that ``STATIC_URL`` is set to
              ``'/static/'``.

    It's assumed that the project's static directory is set up as a
    Node.js package (with a ``package.json`` file & ``node_modules``
    directory) and that the relevant packages are installed via npm.

    ``systemjs.config.js`` must be in the project's top level static
    directory and contain SystemJS config like this::

        (function (global) {
            System.config({
                baseURL: '/static/',
                ...,
            });
        })(this);

    """
    debug = settings.DEBUG
    scripts = []

    if debug:
        scripts.append(staticfiles_storage.url('node_modules/core-js/client/shim.min.js'))
        scripts.append(staticfiles_storage.url('node_modules/systemjs/dist/system.src.js'))
        scripts.append(staticfiles_storage.url('systemjs.config.js'))
    else:
        app_bundle = 'bundles/{app_name}.bundle.js'.format_map(locals())
        scripts.extend(cdn_url(src) for src in cdn_urls)
        scripts.append(staticfiles_storage.url('bundles/angular.bundle.js'))
        scripts.append(staticfiles_storage.url(app_bundle))

    scripts = ['<script src="{src}"></script>'.format(src=s) for s in scripts]

    if debug:
        scripts.append(SYSTEMJS_IMPORT_TEMPLATE % locals())

    scripts = '\n    '.join(scripts)
    return mark_safe(scripts)
