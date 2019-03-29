#!/bin/bash
while :
do
	ps -p 28403 -o %cpu,%mem,cmd
	sleep 1
done
