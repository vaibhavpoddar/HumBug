#!/bin/bash -l

levelName=$1
moves=$2
python3 humbug.py $levelName $moves | grep Success | head -n1 | xargs | sed 's/=>/\n/g'
