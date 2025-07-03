#!/bin/bash
docker exec -i sql-introduction mysql -u root -p'rootpassword' < "$1"
