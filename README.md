# EcoRoofs

A web-mapping application for green roofs in the Portland area.

## Setting up for development

The easiest way to get set up is to install Docker and then run
`make docker-init` and then `make run-docker` (or just the latter, since
it will run the former). `docker-init` will create a service image for
Postgres with PostGIS installed and another image for GeoServer.

You can also set up a local dev environment by running `make init` as
usual.

From this point forward, it's assumed that `make run-docker` is running.
Alternatively, you can run `docker-compose up` directly.

### Testing

Run the following command:

    docker exec -it ecoroofs_ecoroofs_1 /webapps/ecoroofs/venv/bin/python manage.py test

### Migrations

Run the following command:

    docker exec -it ecoroofs_ecoroofs_1 /webapps/ecoroofs/venv/bin/python manage.py migrate

### GeoServer

Unfortunately, you'll still need to go in and manually create some stuff
in GeoServer, but that's not *too* hard:

- Go to http://localhost:8080/geoserver/web/
- Log in with username `admin` and password `geoserver`
- Create a workspace named `ecoroofs`
- Create a PostGIS store in the `ecoroofs` workspace named `ecoroofs`
  - host: `database`
  - database: `ecoroofs`
  - user: `ecoroofs`
  - password: [leave blank]
- Create a `locations` layer from `ecoroofs:ecoroofs`
  - Find the `locations_location` table in the list and click the
    `Publish` link
  - Set the layer's title to `Locations`
  - Scroll and click the two links for automatically computing bounds
