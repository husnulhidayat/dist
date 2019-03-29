#!/bin/bash

secs=300
SECONDS=0

while((SECONDS<secs));
do
	python publish.py -m "heart rate: 66bpm"
done
