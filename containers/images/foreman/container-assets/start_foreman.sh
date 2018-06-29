#!/bin/bash

set -x

scl enable tfm "RAILS_ENV=$RAILS_ENV rails s -b 0.0.0.0 -p 8080"
