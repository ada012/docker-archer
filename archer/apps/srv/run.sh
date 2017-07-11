#!/bin/sh
cd /apps/srv/archer && ./startup.sh
/apps/srv/tengine/sbin/nginx -g 'daemon off;'
