FROM centos:6.7

ENV JAVA_VERSION 1.7.0
ENV JAVA_HOME /usr/lib/jvm/jre-${JAVA_VERSION}

ENV GEOSERVER_VERSION 2.7.1.1
ENV GEOSERVER_DOWNLOAD_URL \
    http://downloads.sourceforge.net/project/geoserver/GeoServer/${GEOSERVER_VERSION}/geoserver-${GEOSERVER_VERSION}-bin.zip?use_mirror=heanet
ENV GEOSERVER_DOWNLOAD_PATH /tmp/geoserver-${GEOSERVER_VERSION}.zip
ENV GEOSERVER_INSTALL_DIR /opt/geoserver-${GEOSERVER_VERSION}
ENV GEOSERVER_HOME ${GEOSERVER_INSTALL_DIR}
ENV GEOSERVER_DATA_DIR /opt/geoserver_data_dir

RUN yum update -y
RUN yum upgrade -y
RUN yum install -y epel-release

RUN yum install -y \
    curl \
    httpd \
    java-${JAVA_VERSION}-openjdk \
    unzip

RUN chkconfig httpd on
COPY etc/httpd/vhost.d/geoserver.conf /etc/httpd/conf.d

RUN adduser -M -s /bin/bash geoserver
RUN test -d ${GEOSERVER_DOWNLOAD_PATH} || curl -L -o ${GEOSERVER_DOWNLOAD_PATH} ${GEOSERVER_DOWNLOAD_URL}
RUN rm -rf ${GEOSERVER_INSTALL_DIR}
RUN unzip -d /opt ${GEOSERVER_DOWNLOAD_PATH}
RUN chown -R geoserver ${GEOSERVER_INSTALL_DIR}
RUN ls -l /opt
RUN ls -l ${GEOSERVER_INSTALL_DIR}

EXPOSE 80
COPY entrypoint.sh /usr/local/bin
ENTRYPOINT /usr/local/bin/entrypoint.sh
