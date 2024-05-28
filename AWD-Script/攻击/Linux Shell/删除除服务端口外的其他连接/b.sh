#!/bin/bash

while true
do
	kill -9 $(netstat -anpt | grep -E '21|23' | grep -v '*' | awk '{print $7}' | awk -F '/' '{print $1}')
	sleep 1
done
