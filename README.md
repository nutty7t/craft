# NuttyCraft

> Deployment through Docker. 12 hour backups.

``` sh
# pull docker image
docker pull nutty7t/craft:1.14.1

# start server
docker run \
	-e BACKUP_CRONJOB='true' \ # optional
	--volume=/path/to/server/files:/minecraft \
	--volume=/path/to/backup/directory:/backups \
	--network=host \
	--name=nuttycraft \
	--detach \
	nutty7t/craft:1.14.1

# stream server logs
docker exec --tty nuttycraft tail -f /minecraft/logs/latest.log

# stream backup logs
docker exec --tty nuttycraft tail -f /var/log/cron.log
```

