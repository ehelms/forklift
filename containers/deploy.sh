#!/bin/bash

ansible-playbook deploy.yml

ansible-playbook ansible-deployment/foreman.yml --tags start
