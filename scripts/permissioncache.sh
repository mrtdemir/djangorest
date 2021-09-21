#!/bin/bash
exec &>> /tmp/api_cache_permission.txt
date > /tmp/date
cd /home/api
chmod -R 755 caches
exit 0