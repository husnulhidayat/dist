#!/bin/bash
while :
do
	ps -p 29618 -o %cpu,%mem,cmd
	sleep 1
done
