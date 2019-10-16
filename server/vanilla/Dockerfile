FROM openjdk:8u201-jre-alpine
RUN apk --no-cache add curl

# ──────────────────────────────────────────────────────────────────────
#  Download Paper Server JAR
# ──────────────────────────────────────────────────────────────────────

ENV MINECRAFT_VERSION=1.14
RUN curl -fsSL -o /server.jar \
	https://papermc.io/ci/job/Paper-${MINECRAFT_VERSION}/lastSuccessfulBuild/artifact/paperclip.jar

# ──────────────────────────────────────────────────────────────────────
#  Start Minecraft Server
# ──────────────────────────────────────────────────────────────────────

WORKDIR /minecraft
CMD ["java", "-jar", "/server.jar"]

