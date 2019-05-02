#!/usr/bin/env sh

# Start cron daemon.
/usr/sbin/crond -l 8

# Start Minecraft server.
java -jar /server.jar

