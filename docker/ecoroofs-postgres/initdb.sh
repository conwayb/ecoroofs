#!/bin/bash
set -e

if [ "${1:0:1}" = "-" ]; then
    set -- postgres "$@"
fi

# This will only be run if a non-postgres COMMAND is passed to Docker.
if [ "$1" != "postgres" ]; then
    # Run some other command if indicated.
    exec "$@"
fi

# Everything below is run by default.
mkdir -p "$PGDATA"
chmod 700 "$PGDATA"
chown -R $PGUSER "$PGDATA"

if [ ! -s "$PGDATA/PG_VERSION" ]; then
    su $PGUSER -c initdb

    # Don't require passwords.
    echo >> "$PGDATA/pg_hba.conf"
    echo "host all all 0.0.0.0/0 trust" >> "$PGDATA/pg_hba.conf"

    # Replaces the default `listen_addresses = 'localhost'` with
    # `listen_addresses = '*'` to allow connections from outside the
    # container.
    sed -ri "s/^#?(listen_addresses)\s*=\s*\S+.*/\1 = '*'/" "$PGDATA/postgresql.conf"

    # Temporary, localhost-only instance for running database
    # initialization commands.
    su $PGUSER <<-EOF
        pg_ctl -D "$PGDATA" -o "-c listen_addresses='localhost'" -w start
EOF

    psql -v ON_ERROR_STOP=1 <<-EOSQL
        CREATE USER ecoroofs WITH SUPERUSER;
        CREATE DATABASE ecoroofs OWNER ecoroofs;
EOSQL

    # The gt_pk_metadata table is used by GeoServer:
    # http://docs.geoserver.org/stable/en/user/data/database/primarykey.html
    psql -v ON_ERROR_STOP=1 ecoroofs <<-EOSQL
        CREATE EXTENSION hstore;
        CREATE EXTENSION postgis;
        CREATE TABLE public.gt_pk_metadata (
            table_schema VARCHAR(32) NOT NULL,
            table_name VARCHAR(32) NOT NULL,
            pk_column VARCHAR(32) NOT NULL,
            pk_column_idx INTEGER,
            pk_policy VARCHAR(32),
            pk_sequence VARCHAR(64),
            unique (table_schema, table_name, pk_column),
            check (pk_policy in ('sequence', 'assigned', 'autoincrement'))
        );
        GRANT ALL PRIVILEGES ON DATABASE ecoroofs TO ecoroofs;
EOSQL

    # Kill temporary instance.
    su $PGUSER -c "pg_ctl -D '$PGDATA' -m fast -w stop"
fi

# Run postgres.
exec su $PGUSER -c "$@"
