#!/usr/bin/make

docker_compose_bin := $(shell command -v docker-compose 2> /dev/null)

run:
	docker-compose -f ./start.yml up -d --build

mysql:
	docker-compose -f ./mysql.yml up -d --build
