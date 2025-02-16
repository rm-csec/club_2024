#!/bin/sh
docker build -t based_lfi .
docker run -d -p 1337:1337 baby_lfi
printf "Chall running on: http://127.0.0.1:1337\n"
