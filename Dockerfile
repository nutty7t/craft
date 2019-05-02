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
#  Start Minecraft Server
# ──────────────────────────────────────────────────────────────────────

WORKDIR /minecraft
CMD ["java", "-jar", "/server.jar"]

