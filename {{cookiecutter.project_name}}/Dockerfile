##################################################################
# Base image
##################################################################
FROM frolvlad/alpine-python3 as base

WORKDIR /src

COPY . ./

RUN pip3 install .

##################################################################
# Builder
##################################################################
FROM base as builder

RUN apk --no-cache add make \
    && pip3 install -e .[dev] \
    && make clean lint scan test

##################################################################
# Runtime
##################################################################
FROM base as release

# Serve http on port 5000
EXPOSE 5000

ENTRYPOINT ["/bin/sh", "scripts/entrypoint.sh"]
