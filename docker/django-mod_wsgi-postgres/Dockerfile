FROM centos:6.7

ENV PATH $PATH:/usr/pgsql-9.4/bin

RUN sed -i -E 's#(\[(base|updates)\])#\1\nexclude=postgresql*#g' /etc/yum.repos.d/CentOS-Base.repo

RUN yum update -y
RUN yum upgrade -y

RUN yum install -y epel-release
RUN yum localinstall -y https://centos6.iuscommunity.org/ius-release.rpm
RUN yum localinstall -y https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-6-x86_64/pgdg-centos94-9.4-3.noarch.rpm
RUN curl --silent --location https://rpm.nodesource.com/setup_6.x | bash -

RUN yum groupinstall -y 'Development Tools'
RUN yum install -y \
    gdal \
    geos \
    git \
    httpd \
    httpd-devel \
    nodejs \
    postgresql94 \
    postgresql94-devel \
    postgresql94-libs \
    proj \
    python35u \
    python35u-devel \
    python35u-mod_wsgi \
    which

RUN yum clean all

RUN /usr/bin/python3.5 -m ensurepip
RUN /usr/bin/pip3 install -U setuptools pip virtualenv mod_wsgi
