#!/usr/bin/env sh

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
printf "[$(date +"%Y-%m-%d %r")] Creating Minecraft Server Backup... "
tar -cpvzf /backups/backup_${TIMESTAMP}.tar.gz /minecraft/* &> /dev/null
echo "complete"

