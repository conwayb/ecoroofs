from arctasks import *
from arctasks.deploy import Deployer
from arctasks.util import abort, print_header


@arctask(configured='dev', timed=True)
def init(ctx, overwrite=False, drop_db=False):
    virtualenv(ctx, overwrite=overwrite)
    install(ctx)
    npm_install(ctx, where='{package}/static', modules=[])
    createdb(ctx, drop=drop_db)
    migrate(ctx)
    sass(ctx)


@arctask(configured='dev')
def build_static(ctx, css=True, css_sources=None, js=True, js_sources=None, collect=True,
                 optimize=True, static_root=None):
    if css:
        build_css(ctx, sources=css_sources, optimize=optimize)
    if js:
        build_js(ctx, sources=js_sources)
    if collect:
        collectstatic(ctx, static_root=static_root)


@arctask(configured='dev', timed=True)
def build_js(ctx, sources=None):
    # TODO: Pass sources to Node script?
    if sources is not None:
        abort(1, 'The --sources option is currently ignored by build_js')
    local(ctx, 'node build.js', cd='{package}/static')


class EcoRoofsDeployer(Deployer):

    def build_static(self):
        print_header('Building static files (EcoRoofs custom)...')
        build_static(self.ctx)


deploy.deployer_class = EcoRoofsDeployer


@arctask(configured='dev', timed=True)
def import_locations(ctx, file_name='locations.csv', overwrite=False, dry_run=False, quiet=False):
    """Import locations from CSV file provided by client."""
    from arctasks.django import setup; setup()
    from ecoroofs.locations.importer import Importer
    location_importer = Importer(file_name, overwrite=overwrite, dry_run=dry_run, quiet=quiet)
    location_importer.run()
