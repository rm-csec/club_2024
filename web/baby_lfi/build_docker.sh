#!/bin/sh
docker build -t baby_lfi .
docker run -d -p 5000:5000 baby_lfi
printf "Chall running on: http://127.0.0.1:5000\n"
