#!/bin/bash

set -x

#scl enable rh-ruby24 "RAILS_ENV=development rails s -b 0.0.0.0 -p 8080"
scl enable rh-ruby24 'BIND=0.0.0.0 foreman start'
