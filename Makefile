#
build:
	docker-compose -f docker/docker-compose.yml build

build-nc:
	docker-compose -f docker/docker-compose.yml build --no-cache

up:
	docker-compose -f docker/docker-compose.yml up

up-db:
	docker-compose -f docker/docker-compose-db.yml up

down:
	docker-compose -f docker/docker-compose.yml down

run:
	docker-compose -f docker/docker-compose.yml run airflow-worker $(c)

shell:
	docker run -it docker_airflow-worker bash
