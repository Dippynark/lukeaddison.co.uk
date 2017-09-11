############################################################
# Dockerfile to run lukeaddison.co.uk
# Based on a Python 3.6 Image
############################################################

FROM python:3.6

LABEL maintainer "Luke Addison"

RUN apt-get update && apt-get install -y \
  npm \
  git \
  && rm -rf /var/lib/apt/lists/*

RUN npm install less -g

# Debian installs node as nodejs
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10

ENV SRCROOT=/usr/src/app
WORKDIR $SRCROOT

COPY requirements.txt $SRCROOT
RUN pip install --no-cache-dir -r requirements.txt && rm -f requirements.txt
# Patch mezzanine_pagedown module
RUN sed -i 's/settings.RICHTEXT_ALLOWED_ATTRIBUTES/list(settings.RICHTEXT_ALLOWED_ATTRIBUTES)/' /usr/local/lib/python3.6/site-packages/mezzanine_pagedown/filters.py

COPY manage.py $SRCROOT
COPY lukeaddison_co_uk $SRCROOT/lukeaddison_co_uk
COPY theme $SRCROOT/theme
RUN ln -s $SRCROOT/lukeaddison_co_uk/local/local_settings.py $SRCROOT/lukeaddison_co_uk/local_settings.py 

RUN mkdir static logs
VOLUME ["$SRCROOT/static/", "$SRCROOT/logs/", "$SRCROOT/lukeaddison_co_uk/local"]

# Port to expose
EXPOSE 8000

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
