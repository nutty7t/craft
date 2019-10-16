IMG_NAME       ?= nutty7t/minecraft-ftb-server
IMG_TAG        ?= latest
CONTAINER_NAME ?= nuttycraft-ftb
DATA_DIR       ?= data
ABS_DATA_DIR   := ${CURDIR}/../$(DATA_DIR)

image:
	docker build --tag $(IMG_NAME):$(IMG_TAG) $(DOCKER_ARGS) .

push:
	docker push $(IMG_NAME):$(IMG_TAG)

start:
	# Creating data directory (if not existing).
	mkdir -p $(ABS_DATA_DIR)
	docker run \
		--volume=$(ABS_DATA_DIR):/minecraft \
		--name=$(CONTAINER_NAME) \
		--detach \
		$(DOCKER_ARGS) \
		$(IMG_NAME):$(IMG_TAG)

stop:
	# We're just going to assume that you were a good boy
	# and mounted a volume in order to persist server data.
	docker rm --force $(CONTAINER_NAME) || true

logs:
	@ # Try streaming the logs first. If that doesn't work,
	@ # then the container is probably not running. In that
	@ # case, just try to output the logs.
	@ docker exec --tty $(CONTAINER_NAME) tail -f /minecraft/logs/latest.log || \
		docker container logs $(CONTAINER_NAME)

.PHONY: image push start stop logs

