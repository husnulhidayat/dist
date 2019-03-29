#!/bin/bash

secs=300
SECONDS=0

while((SECONDS<secs));
do
	./publish -m "heart rate: 66bpm"

done
