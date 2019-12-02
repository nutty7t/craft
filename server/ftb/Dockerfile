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
COPY mods/Hats-4.0.1.jar mods/Hats-4.0.1.jar

# Install additional mods.
COPY mods/ mods/

# Set the fml.queryResult=confirm environment variable when starting the server.
# While adding additional mods to FTB Infinity Evolved, I ran into the following
# warning:
#
# > There are 1 missing blocks and items in this save.
# > If you continue the missing blocks/items will get removed.
# > A world backup will be automatically created in your saves directory.
#
# > Missing Blocks/Items:
# > aobd:dustSteel
#
# > Run the command /fml confirm or /fml cancel to proceed.
# > Alternatively start the server with -Dfml.queryResult=confirm or
# > -Dfml.queryResult=cancel to preselect the answer.
#
# This will non-interactively confirm the warning.
RUN sed -i 's/-server/-server -Dfml.queryResult=confirm/' ServerStart.sh

# ──────────────────────────────────────────────────────────────────────
#  Start FTB Server
# ──────────────────────────────────────────────────────────────────────

CMD ["/bin/sh", "/minecraft/ServerStart.sh", "-Dfml.queryResult=confirm"]

