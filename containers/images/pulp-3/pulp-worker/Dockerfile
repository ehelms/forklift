FROM pulpcore:latest

RUN echo "tsflags=nodocs" >> /etc/yum.conf && \
		yum -y install git && \
		yum clean all

ENV LC_ALL=en_US.utf-8
ENV LANG=en_US.utf-8

COPY container-assets/wait_on_database_migration.py /usr/bin/wait_on_database_migration.py
COPY container-assets/pulp-worker /usr/bin/pulp-worker
COPY container-assets/entrypoint /usr/bin/entrypoint

CMD ["/usr/bin/pulp-worker"]
ENTRYPOINT ["/usr/bin/entrypoint"]
