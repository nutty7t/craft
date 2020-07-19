FROM openjdk:8u201-jre-alpine
RUN apk --no-cache add curl

# ──────────────────────────────────────────────────────────────────────
#  Download FTB Revelation
# ──────────────────────────────────────────────────────────────────────

WORKDIR /minecraft
RUN curl -fsSL -o ftb-revelation-server.zip \
	https://media.forgecdn.net/files/2778/975/FTBRevelationServer_3.2.0.zip

RUN unzip ftb-revelation-server.zip \
	&& rm ftb-revelation-server.zip \
	&& echo "eula=TRUE" > eula.txt \
	&& chmod +x ServerStart.sh

COPY server.properties .

# Install additional mods.
COPY mods/ mods/

# ──────────────────────────────────────────────────────────────────────
#  Start FTB Server
# ──────────────────────────────────────────────────────────────────────

CMD ["/bin/sh", "/minecraft/ServerStart.sh", "-Dfml.queryResult=confirm"]
