# EcoRoofs

A web-mapping application for green roofs in the Portland area.

## Setting up for development

The easiest way to get set up is to install Docker and then run
`make docker-init` and then `make run-docker` (or just the latter, since
it will run the former). `docker-init` will create a service image for
Postgres with PostGIS installed and another image for GeoServer.

You can also set up a local dev environment by running `make init` as
usual. This is useful for running some commands locally even when using
Docker.

If you don't want to use Docker for development, you'll have to set up
Postgres and GeoServer manually.

From this point forward, it's assumed that `make run-docker` is running.
Alternatively, you can run `docker-compose up` directly.

### Testing

Run the following command:

    docker exec -it ecoroofs_ecoroofs_1 /webapps/ecoroofs/venv/bin/python manage.py test

### Migrations

Run the following command:

    docker exec -it ecoroofs_ecoroofs_1 /webapps/ecoroofs/venv/bin/python manage.py migrate

### Importing Data

Location data is stored in the git repo. Neighborhood data needs be
downloaded from Metro's RLIS Discovery site first:

    http://rlisdiscovery.oregonmetro.gov/?action=viewDetail&layerID=237

and extracted into `./rlis/nbo_hood`.

Then run the following command:

    docker exec -it ecoroofs_ecoroofs_1 /webapps/ecoroofs/venv/bin/inv configure -e docker import_all

### GeoServer

Unfortunately, you'll still need to go in and manually create some stuff
in GeoServer, but that's not *too* hard:

- Go to http://localhost:8080/geoserver/web/
- Log in with username `admin` and password `geoserver`
- Create a workspace named `ecoroofs`
- Create a PostGIS store in the `ecoroofs` workspace named `ecoroofs`
  - host: `database` (this is the host name configured via Docker
    Compose)
  - database: `ecoroofs`
  - user: `ecoroofs`
  - password: [leave blank]
- Create a `locations` layer from `ecoroofs:ecoroofs`
  - Find the `locations_location` table in the list and click the
    `Publish` link
  - Set the layer's name to `locations`
  - Set the layer's title to `Locations`
  - Scroll and click the two links for automatically computing bounds
- Create a `neighborhoods` layer from `ecoroofs:ecoroofs`
  - Find the `neighborhoods_neighborhood` table in the list and click the
    `Publish` link
  - Set the layer's name to `neighborhoods`
  - Set the layer's title to `Neighborhoods`
  - Scroll and click the two links for automatically computing bounds
