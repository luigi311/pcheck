#! /bin/bash

dockps="$(docker ps -a | awk 'FNR == 2 {print $1}')"
docker rm $dockps
docker rmi pcheck
