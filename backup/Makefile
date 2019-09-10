IMG_NAME       ?= nutty7t/minecraft-backup
IMG_TAG        ?= latest
DATA_DIR       ?= data
BACKUP_DIR     ?= backups
ABS_DATA_DIR   := ${CURDIR}/../$(DATA_DIR)
ABS_BACKUP_DIR := ${CURDIR}/../$(BACKUP_DIR)

requirements.txt:
	pipenv lock -r > requirements.txt

image: requirements.txt
	docker build --tag $(IMG_NAME):$(IMG_TAG) $(DOCKER_ARGS) .

push:
	docker push $(IMG_NAME):$(IMG_TAG)

backup:
	# Creating backup directory (if not existing).
	mkdir -p $(ABS_BACKUP_DIR)
	docker run \
		--volume=$(ABS_DATA_DIR):/minecraft \
		--volume=$(ABS_BACKUP_DIR):/backups \
		$(DOCKER_ARGS) \
		$(IMG_NAME):$(IMG_TAG)

.PHONY: image push backup

