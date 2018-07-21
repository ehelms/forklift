FROM docker.io/shurley/ansible-operator

RUN echo "retry_files_enabled = false" >> /etc/ansible/ansible.cfg
RUN echo "stdout_callback = actionable" >> /etc/ansible/ansible.cfg

RUN adduser -D ansible-operator
USER ansible-operator

COPY roles/ /opt/ansible/roles/
COPY playbook.yaml /opt/ansible/roles/playbook.yaml
COPY config.yaml /opt/ansible/config.yaml
