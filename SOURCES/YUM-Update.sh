#!/bin/sh
if [ ! -f /var/lock/subsys/yum ]; then
  /usr/bin/yum -R 10 -e 0 -d 1 -y update yum
  /usr/bin/yum -R 120 -e 0 -d 1 -y update
fi
