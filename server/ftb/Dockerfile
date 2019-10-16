FROM openjdk:8u201-jre-alpine
RUN apk --no-cache add curl

# ──────────────────────────────────────────────────────────────────────
#  Download FTB Infinity Evolved
# ──────────────────────────────────────────────────────────────────────

WORKDIR /minecraft
RUN curl -fsSL -o ftb-infinity-server.zip \
	https://media.forgecdn.net/files/2731/545/FTBInfinityServer_3.1.0.zip

RUN unzip ftb-infinity-server.zip \
	&& rm ftb-infinity-server.zip \
	&& echo "eula=TRUE" > eula.txt \
	&& chmod +x FTBInstall.sh ServerStart.sh \
	&& ./FTBInstall.sh

# ──────────────────────────────────────────────────────────────────────
#  Start FTB Server
# ──────────────────────────────────────────────────────────────────────

CMD ["/bin/bash", "/minecraft/ServerStart.sh"]

