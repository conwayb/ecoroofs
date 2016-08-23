#!/bin/bash
service httpd start
exec /opt/geoserver-2.7.1.1/bin/startup.sh
