#!/bin/sh
for Dir in $(find -maxdepth 1 -type d | sed '1d')
do
    NewDir=$(cat /proc/sys/kernel/random/uuid | cksum | cut -f1 -d" ")
    while [ -d $NewDir ]
    do
        NewDir=$(cat /proc/sys/kernel/random/uuid | cksum | cut -f1 -d" ")
    done
    mv $Dir $NewDir
done
