include .env

up:
	docker run -p ${BACKEND_TARGET_PORT}:${BACKEND_PUBLISHED_PORT} app

down:
	docker system prune && \
	docker image rm app

build:
	docker build -t app .
