FROM centos:6.7

ENV PATH /usr/pgsql-9.4/bin:$PATH
ENV PGDATA /var/lib/pgsql/9.4/data
ENV PGUSER postgres

RUN yum update -y
RUN yum upgrade -y
RUN yum install -y epel-release
RUN yum localinstall -y https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-6-x86_64/pgdg-centos94-9.4-3.noarch.rpm

RUN yum install -y \
    postgresql94 \
    postgresql94-contrib \
    postgresql94-libs \
    postgresql94-server \
    postgis2_94 \
    postgis2_94-client

RUN yum clean all

RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./initdb.sh /docker-entrypoint-initdb.d

CMD ["postgres"]
ENTRYPOINT ["/docker-entrypoint-initdb.d/initdb.sh"]
EXPOSE 5432
VOLUME $PGDATA
