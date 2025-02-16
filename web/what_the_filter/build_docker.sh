#!/bin/sh
docker build -t what_the_filter .
docker run -d -p 9999:9999 what_the_filter
printf "Chall running on: http://127.0.0.1:9999\n"
