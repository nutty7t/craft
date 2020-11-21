FROM openjdk:8u201-jre-alpine
RUN apk --no-cache add curl

# ──────────────────────────────────────────────────────────────────────
#  Download GregTech: New Horizons
# ──────────────────────────────────────────────────────────────────────

WORKDIR /minecraft
RUN curl -o ftb-gtnh-server.zip \
	http://downloads.gtnewhorizons.com/ServerPacks/GTNewHorizonsServer-1.7.10-2.0.9.0.zip

RUN unzip ftb-gtnh-server.zip \
	&& rm ftb-gtnh-server.zip \
	&& echo "eula=TRUE" > eula.txt \
	&& chmod +x startserver.sh

COPY server.properties .

# ──────────────────────────────────────────────────────────────────────
#  Link Start!
# ──────────────────────────────────────────────────────────────────────

CMD ["/bin/sh", "/minecraft/startserver.sh", "-Dfml.queryResult=confirm"]
