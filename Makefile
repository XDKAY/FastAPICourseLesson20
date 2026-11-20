DOCKER_IMAGE_NAME=fastapi_course_lesson20
.PHONY: build run logs start stop clean


build:
	docker build -t $(DOCKER_IMAGE_NAME) .

run:
	docker run -d -p 8000:80 --env-file .env $(DOCKER_IMAGE_NAME)

logs:
	docker container logs $$(docker ps -a --filter ancestor=$(DOCKER_IMAGE_NAME) -q)

start:
	docker start $$(docker ps -a --filter ancestor=$(DOCKER_IMAGE_NAME) -q)

stop:
	docker stop $$(docker ps -a --filter ancestor=$(DOCKER_IMAGE_NAME) -q)

clean:
	docker rm $$(docker ps -a --filter ancestor=$(DOCKER_IMAGE_NAME) -q)
	docker rmi $$(docker images --filter reference=$(DOCKER_IMAGE_NAME) -q)
