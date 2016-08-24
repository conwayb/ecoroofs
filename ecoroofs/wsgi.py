import os
import site
import sys


def create_wsgi_application(default_django_settings_module=None):
    """Create a WSGI application.

    Args:
        default_django_settings_module: This will be used if the
            ``DJANGO_SETTINGS_MODULE`` environment variable isn't set.
            If neither of these is set, the settings module will be
            set to ``'{directory containing wsgi.py}.settings'``.

    """
    # Directory containing this wsgi.py file.
    containing_dir = os.path.dirname(__file__)

    # Just the base name (with no path) of the containing directory.
    dir_name = os.path.basename(containing_dir)

    # The top level project directory, assuming that this wsgi.py file is in
    # the project's top level package directory.
    default_root = os.path.dirname(containing_dir)

    if default_django_settings_module is None:
        default_django_settings_module = '{dir_name}.settings'.format_map(locals())

    root = os.environ.get('WSGI_ROOT', default_root)
    venv = os.environ.get('WSGI_VENV', os.path.join(root, '.env'))

    major, minor = sys.version_info[:2]
    site_packages_rel_path = 'lib/python{major}.{minor}/site-packages'.format(**locals())
    site_packages = os.path.join(venv, site_packages_rel_path)

    if not os.path.isdir(site_packages):
        raise NotADirectoryError(
            'Could not find virtualenv site-packages at {}'.format(site_packages))

    # Add the virtualenv's site-packages to sys.path, ensuring its packages
    # take precedence over system packages (by moving them to the front of
    # sys.path after they're added).
    old_sys_path = list(sys.path)
    site.addsitedir(site_packages)
    new_sys_path = [item for item in sys.path if item not in old_sys_path]
    sys.path = new_sys_path + old_sys_path

    os.environ.setdefault('LOCAL_SETTINGS_FILE', os.path.join(root, 'local.cfg'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', default_django_settings_module)

    from django.conf import settings
    from django.core.management import call_command
    from django.core.wsgi import get_wsgi_application

    app = get_wsgi_application()

    if not settings.DEBUG:
        from arcutils.tasks import DailyTasksProcess
        daily_tasks = DailyTasksProcess(home=root)
        daily_tasks.add_task(call_command, 3, 1, ('clearsessions',), name='clearsessions')
        daily_tasks.start()

    return app


application = create_wsgi_application('ecoroofs.settings')
