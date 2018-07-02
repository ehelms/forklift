#!/bin/bash

set -x

ansible-playbook playbooks/wait_on_postgres.yaml
ansible-playbook playbooks/configure_database.yaml

cd katello

scl enable rh-ruby24 "npm install"

cd ../foreman

scl enable rh-ruby24 "bundle update"
scl enable rh-ruby24 "npm install"
scl enable rh-ruby24 "rake db:migrate"
scl enable rh-ruby24 "SEED_ADMIN_PASSWORD=changeme rake db:seed"

exec "$@"
