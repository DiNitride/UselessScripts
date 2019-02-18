#!/bin/bash

SERVICES=()

for i in "${SERVICES[@]}"
do
   :
   printf "%-20.20s" $i
   if systemctl is-active --quiet $i
   then
     echo ACTIVE
   else
     echo Inactive
   fi
done
