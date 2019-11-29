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

COPY server.properties .

# Patch the Hats mod by iChunUtil. Replace HTTP requests with HTTPS requests.
# CDNs disallow HTTP requests according to the patch notes:
# https://github.com/RedstoneTek/HatsDownloader
COPY Hats-4.0.1.jar mods/Hats-4.0.1.jar

# ──────────────────────────────────────────────────────────────────────
#  Start FTB Server
# ──────────────────────────────────────────────────────────────────────

CMD ["/bin/sh", "/minecraft/ServerStart.sh"]

