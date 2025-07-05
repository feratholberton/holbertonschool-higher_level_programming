#!/bin/bash
docker  exec --interactive sql-more-queries\
        mysql -u'root' -p'rootpassword'\
        < "$1" "$2"
