# NuttyCraft

![nuttycraft](https://user-images.githubusercontent.com/40926021/58226814-34fb1e80-7cdd-11e9-881b-48fa556ed033.png)

``` sh
# build docker images
# (requires make, docker, and pipenv)
make all

# start the server
make -C server start

# stop the server
make -C server stop

# stream server logs
make -C server logs

# backup the server
make -C backup backup
```

Take a look [here](https://github.com/nutty7t/os/blob/master/k8s/minecraft.yaml) to see how I am using deploying these Docker images in Kubernetes.

- `backup` runs as a Kubernetes CronJob that performs scheduled backups of the server.
- `restore` runs as an init container that enables restoration of backup archives to persistent volumes.
- `server` runs as a pod container which runs the Minecraft server.
