#!/bin/bash
docker exec --interactive sql-introduction\
 mysql -u'root' -p'rootpassword'\
 < "$1" "$2"
