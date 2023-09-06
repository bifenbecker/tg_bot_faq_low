include .common.env
$(eval export $(shell sed -ne 's/ *#.*$$//; /./ s/=.*$$// p' .env))

DOCKER_USERNAME ?= bifenbecker
IMAGE_NAME ?= ${DOCKER_USERNAME}/${PROJECT__NAME}-${PROJECT__ENV}:${PROJECT__VERSION}
CONTAINER_NAME ?= ${DOCKER_USERNAME}-${PROJECT__NAME}-${PROJECT__ENV}-${PROJECT__VERSION}

merge-envs:
	sort -u -t '=' -k 1,1 ./config/env/.env ./deploy/.compose.env > .common.env

build:
	 docker build --tag ${IMAGE_NAME}  -f . .

compose: merge-envs
	docker-compose --env-file .common.env -p ${CONTAINER_NAME} --profile ${DOCKER_USERNAME} up -d --remove-orphans

compose-build: merge-envs
	docker-compose --env-file .common.env -p ${CONTAINER_NAME} --profile ${DOCKER_USERNAME} up -d --build --remove-orphans

pgb:
	docker secret create pg_bouncer_auth_file ./deploy/pb_bouncer_auth_file.txt

pgb-update:
	docker secret rm pg_bouncer_auth_file
	docker secret create pg_bouncer_auth_file ./deploy/pb_bouncer_auth_file.txt