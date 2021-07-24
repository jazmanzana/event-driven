run:
	docker-compose up -d

restart:
	docker rm $(CONTAINER) && docker image rm event-driven_app && docker-compose up

clean:
	docker rm -f $$(docker ps -a -q) && docker rmi -f $$(docker images -a -q)