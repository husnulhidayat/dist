#!/bin/bash
while :
do
	ps -p 30604 -o %cpu,%mem,cmd
	sleep 1
done
