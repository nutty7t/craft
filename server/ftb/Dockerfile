FROM openjdk:8u201-jre-alpine
RUN apk --no-cache add curl

# ──────────────────────────────────────────────────────────────────────
#  Download GregTech: New Horizons
# ──────────────────────────────────────────────────────────────────────

WORKDIR /minecraft
RUN curl -o ftb-gtnh-server.zip \
	http://downloads.gtnewhorizons.com/ServerPacks/GTNewHorizonsServer-1.7.10-2.1.0.0.zip

RUN unzip ftb-gtnh-server.zip \
	&& rm ftb-gtnh-server.zip \
	&& echo "eula=TRUE" > eula.txt \
	&& chmod +x startserver.sh

RUN sed -i 's/-jar/-Dfml.queryResult=confirm -jar/' startserver.sh

COPY server.properties .
COPY whitelist.json .

# ──────────────────────────────────────────────────────────────────────
#  Link Start!
# ──────────────────────────────────────────────────────────────────────

CMD ["/bin/sh", "/minecraft/startserver.sh", "-Dfml.queryResult=confirm"]
