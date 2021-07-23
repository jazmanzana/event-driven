run:
	docker-compose up -d

restart:
	docker rm $(CONTAINER) && docker image rm event-driven_app && docker-compose up