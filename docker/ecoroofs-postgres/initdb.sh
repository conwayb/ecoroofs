#!/bin/bash
set -e

export PGUSER="$POSTGRES_USER"

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
