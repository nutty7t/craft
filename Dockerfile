FROM openjdk:8u201-jre-alpine
RUN apk --no-cache add curl jq

# ──────────────────────────────────────────────────────────────────────
#  Download Minecraft Server JAR
# ──────────────────────────────────────────────────────────────────────

ENV MINECRAFT_VERSION=1.14
RUN curl -fsSL https://launchermeta.mojang.com/mc/game/version_manifest.json \
	| jq -r ".versions[] | select(.id == \"$MINECRAFT_VERSION\") | .url" \
	| xargs curl -fsSL \
	| jq -r ".downloads.server.url" \
	| xargs curl -fsSL -o /server.jar

# ──────────────────────────────────────────────────────────────────────
#  Configure Backup Cron Job
# ──────────────────────────────────────────────────────────────────────

COPY backup.sh /backup.sh
COPY crontab.txt /crontab.txt
COPY entrypoint.sh /entrypoint.sh
RUN touch /var/log/cron.log
RUN /usr/bin/crontab /crontab.txt
RUN chmod 755 /entrypoint.sh /backup.sh

# ──────────────────────────────────────────────────────────────────────
#  Start Minecraft Server
# ──────────────────────────────────────────────────────────────────────

WORKDIR /minecraft
ENTRYPOINT ["/entrypoint.sh"]

