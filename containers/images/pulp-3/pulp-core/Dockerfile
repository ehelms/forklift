FROM centos:7

RUN echo "tsflags=nodocs" >> /etc/yum.conf && \
		yum -y install epel-release centos-release-scl && \
		yum -y install wget git rh-python36-python-pip && \
		yum clean all

ENV PYTHONUNBUFFERED=0
ENV DJANGO_SETTINGS_MODULE=pulpcore.app.settings

RUN mkdir -p /etc/pulp
COPY container-assets/server-build.yaml /etc/pulp/server.yaml

WORKDIR /root
RUN git clone https://github.com/pulp/pulp.git
RUN git clone https://github.com/pulp/pulp_file.git
RUN git clone https://github.com/pulp/pulp_ansible.git

# Work around for logging to console -- https://pulp.plan.io/issues/3879
COPY container-assets/settings.py /root/pulp/pulpcore/pulpcore/app/settings.py

WORKDIR /root/pulp
RUN scl enable rh-python36 'pip install -e pulpcore/'
RUN scl enable rh-python36 'pip install -e common/'
RUN scl enable rh-python36 'pip install -e plugin/'

WORKDIR /root/pulp_file
RUN scl enable rh-python36 'pip install -e .'

WORKDIR /root/pulp_ansible
RUN scl enable rh-python36 'pip install -e .'

RUN scl enable rh-python36 "pulp-manager makemigrations pulp_app"
RUN scl enable rh-python36 "pulp-manager makemigrations pulp_file"
RUN scl enable rh-python36 "pulp-manager makemigrations pulp_ansible"

COPY container-assets/server.yaml /etc/pulp/server.yaml
RUN echo "SECRET_KEY: '`cat /dev/urandom | tr -dc 'a-z0-9!@#$%^&*(\-_=+)' | head -c 50`'" >> /etc/pulp/server.yaml

COPY container-assets/wait_on_postgres.py /usr/bin/wait_on_postgres.py
COPY container-assets/pulp_server /usr/bin/pulp_server
COPY container-assets/entrypoint /usr/bin/entrypoint

CMD ["/usr/bin/pulp_server"]
ENTRYPOINT ["/usr/bin/entrypoint"]
