run-infra:
	docker-compose up db queues

run-app:
	docker-compose up app worker

restart:
	docker rm $(CONTAINER) && docker image rm event-driven_worker && docker-compose up

clean-all:
	docker rm -f $$(docker ps -a -q) && docker rmi -f $$(docker images -a -q)

test:
	python -m pytest

lint:
	black .