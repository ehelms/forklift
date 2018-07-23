FROM centos:7

RUN echo "tsflags=nodocs" >> /etc/yum.conf && \
		yum -y install epel-release && \
		yum -y install redis && \
		yum clean all

CMD /usr/bin/redis-server --protected-mode no
