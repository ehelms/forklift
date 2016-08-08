#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author: Clint Savage- @herlo <herlo1@gmail.com>
#
# Manage the spin up of duffy nodes.
# See https://wiki.centos.org/QaWiki/CI/Duffy for more information about
# duffy.
#

#---- Documentation Start ----------------------------------------------------#
DOCUMENTATION = '''
---
version_added: "0.1"
module: duffy
short_description: Duffy instance managemer
description:
  - This module allows a user to manage any number of duffy systems.
options:
  name:
    description:
      Given name for task
  state:
    description:
      Allocate or Deallocate instances
    required: true
  group:
    description:
      Group to which machine belongs. Useful when provisioning multiple machines
    default: name
  count:
    description:
      Number of instances to allocate
    default: 1
  key_path:
    description:
      Path to duffy.key
    default: ~/duffy.key
  version:
    description:
      Version of CentOS to provision
    choices: [5, 6, 7]
    default: 7
  arch:
    description:
    choices: [ 'x86_64', 'i386' ]
    default: 'x86_64'
notes:
  - See https://wiki.centos.org/QaWiki/CI/Duffy for more information
    required: true
requirements: []
author: Clint Savage - @herlo
'''

EXAMPLES = '''
- name: "provision nodes in group herlo-ci"
  duffy:
    state: present
    count: 4
    group: herlo-ci
# teardown any nodes in group 'herlo-ci'
- name: "teardown openshift nodes"
  duffy:
    state: absent
    group: herlo-ci
'''

#---- Logic Start ------------------------------------------------------------#
import json, urllib, subprocess, sys, os, time

from ansible.constants import mk_boolean
from ansible.module_utils.basic import *


class Duffy:

    def __init__(self):
        pass

    def deallocate(self):
        b=urllib.urlopen(self.done_url).read()

        return {'status': b}

    def allocate(self):
        url=urllib.urlopen(self.get_url)

        try:
            b=json.load(url)
        except ValueError as e:
            raise Exception("The URL '{}' is malformed".format(self.get_url))

#        b={"hosts": ["n58.dusty.ci.centos.org", "n62.dusty.ci.centos.org"], "ssid": "e1c2d56e"}
        hosts=b['hosts']
        ssid=b['ssid']

        return hosts, ssid

    def execute(self, module):

        json_output = {}
        state = module.params['state']
        url_base="http://admin.ci.centos.org:8080"
        api_key=open(os.path.expanduser(module.params['key_path'])).read().strip()

        # allocate some systems if state is 'present' :)
        if state == 'present':

            ver=module.params['version']
            arch=module.params['arch']
            count=module.params['count']

            self.get_url="{0}/Node/get?key={1}&ver={2}&arch={3}&count={4}".format(url_base,api_key,ver,arch,count)
            (hosts, ssid) = self.allocate()
            json_output['hosts'] = hosts
            json_output['ssid'] = ssid

            return json_output
        elif state == 'absent':

            if not module.params.get('ssid'):
                module.fail_json(msg=str("The 'ssid' parameter is required."))

            ssid=module.params['ssid']

            self.done_url="{0}/Node/done?key={1}&ssid={2}".format(url_base,api_key,ssid)
            return self.deallocate()

def main():

    module = AnsibleModule(
        argument_spec=dict(
            name = dict(type='str'),
            state = dict(choices=['present', 'status', 'absent']),
            count = dict(default=1, type='int'),
            ssid = dict(default=None, type='str'),
            version = dict(default=7, type='int'),
            arch = dict(default='x86_64', type='str'),
            key_path = dict(default='~/duffy.key', type='str'),
        ),
    )


    try:
        d = Duffy()
        execute_output = d.execute(module)

        json_output = {}
        hosts = execute_output.get('hosts')
        status = execute_output.get('status')
        if hosts or status is not None:
            json_output['changed'] = True
            json_output.update(execute_output)
        else:
            json_output['changed'] = False

        module.exit_json(**json_output)
    except Exception as e:
        module.fail_json(msg=str(e))


#---- Import Ansible Utilities (Ansible Framework) ---------------------------#
main()
