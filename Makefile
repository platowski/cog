ARCH := $(shell uname -m)
DOCKER_COMPOSE_FILES := -f ./docker-compose.yml
ifeq ($(ARCH), arm64)
	DOCKER_COMPOSE_FILES := -f ./docker-compose.yml -f ./docker-compose.arm-overrides.yml
endif

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d -delete

init:
	cp src/.env.dist src/.env

backend_build:
	docker-compose ${DOCKER_COMPOSE_FILES} build

build:
	make backend_build

backend_up:
	docker-compose ${DOCKER_COMPOSE_FILES} up $(ARGS)


down:
	docker-compose ${DOCKER_COMPOSE_FILES} down --volumes

test:
	docker-compose  ${DOCKER_COMPOSE_FILES} run app pytest


run_black:
	poetry run blackd

it_run:
	make backend_up ARGS="-d"