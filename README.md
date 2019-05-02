# NuttyCraft

> Deployment through Docker. 12 hour backups.

``` sh
# clone repo
git clone https://github.com/nutty7t/craft && cd craft

# build image
docker build --tag nuttycraft .

# start server
docker run \
	--volume=/path/to/server/files:/minecraft \
	--volume=/path/to/backup/directory:/backups \
	--network=host \
	--name=nuttycraft \
	--detach \
	nuttycraft:latest

# stream server logs
docker exec --tty nuttycraft tail -f /minecraft/logs/latest.log

# stream backup logs
docker exec --tty nuttycraft tail -f /var/log/cron.log
```

