#!/bin/bash
exec &>> /tmp/api_list_permission.txt
date > /tmp/date
cd /home/api/productlist
chmod -R 755 urunlist
exit 0