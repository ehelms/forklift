FROM centos:7

RUN echo "tsflags=nodocs" >> /etc/yum.conf && \
    yum -y install epel-release && \
    yum -y install openssl rpm-build git python-pip && \
    yum clean all

WORKDIR /root

RUN pip install setuptools --upgrade
RUN pip install openshift ansible

COPY container-assets/certificates /root/roles/certificates
COPY container-assets/client-rpm /root/roles/client-rpm
COPY container-assets/build.yml /root/build.yml

COPY container-assets/deploy/secrets.yml /root/deploy/secrets.yml
COPY container-assets/deploy.yml /root/deploy.yml

CMD ["ansible-playbook"]
