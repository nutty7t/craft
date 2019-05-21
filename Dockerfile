FROM openjdk:8u201-jre-alpine
RUN apk --no-cache add curl jq

# ──────────────────────────────────────────────────────────────────────
#  Download Paper Server JAR
# ──────────────────────────────────────────────────────────────────────

ENV MINECRAFT_VERSION=1.14
RUN curl -fsSL -o /server.jar \
	https://papermc.io/ci/job/Paper-${MINECRAFT_VERSION}/lastSuccessfulBuild/artifact/paperclip.jar

# ──────────────────────────────────────────────────────────────────────
#  Configure Backup Cron Job
# ──────────────────────────────────────────────────────────────────────

ENV BACKUP_CRONJOB=false
COPY backup.sh /backup.sh
COPY crontab.txt /crontab.txt
COPY entrypoint.sh /entrypoint.sh
RUN if [ "${BACKUP_CRONJOB}" == "true" ];       \
	then                                        \
		touch /var/log/cron.log                 \
		&& /usr/bin/crontab /crontab.txt        \
		&& chmod 755 /entrypoint.sh /backup.sh; \
	fi

# ──────────────────────────────────────────────────────────────────────
#  Start Minecraft Server
# ──────────────────────────────────────────────────────────────────────

WORKDIR /minecraft
ENTRYPOINT ["/entrypoint.sh"]

