FROM pulpcore:latest

RUN echo "tsflags=nodocs" >> /etc/yum.conf && \
		yum -y install git && \
		yum clean all

#RUN scl enable rh-python36 "pip install -e git+https://github.com/rq/rq.git@3133d94b58e59cb86e8f4677492d48b2addcf5f8#egg=rq"

ENV LC_ALL=en_US.utf-8
ENV LANG=en_US.utf-8

COPY container-assets/wait_on_database_migration.py /usr/bin/wait_on_database_migration.py
COPY container-assets/pulp-resource-manager /usr/bin/pulp-resource-manager
COPY container-assets/entrypoint /usr/bin/entrypoint

CMD ["/usr/bin/pulp-resource-manager"]
ENTRYPOINT ["/usr/bin/entrypoint"]
