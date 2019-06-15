IMG_NAME ?= nutty7t/minecraft-restore
IMG_TAG  ?= latest

image: requirements.txt
	docker build --tag $(IMG_NAME):$(IMG_TAG) $(DOCKER_ARGS) .

push:
	docker push $(IMG_NAME):$(IMG_TAG)

requirements.txt:
	pipenv lock -r > requirements.txt

clean:
	rm -f requirements.txt

.PHONY: image push clean

