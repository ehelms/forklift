FROM centos/ruby-24-centos7

USER root

RUN yum -y install epel-release && \
		yum -y install libvirt-devel systemd-devel ansible qpid-cpp-client-devel && \
    yum clean all

COPY container-assets/entrypoint.sh /usr/bin/entrypoint.sh
COPY container-assets/start_foreman.sh /usr/bin/start_foreman.sh

RUN mkdir playbooks
COPY container-assets/wait_on_postgres.yaml playbooks/wait_on_postgres.yaml
COPY container-assets/configure_database.yaml playbooks/configure_database.yaml

RUN git clone https://github.com/theforeman/foreman
RUN cd foreman && scl enable rh-ruby24 'bundle install'
RUN cd foreman && scl enable rh-ruby24 'npm -g install'

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD ["/usr/bin/start_foreman.sh"]
