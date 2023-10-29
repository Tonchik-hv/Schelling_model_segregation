FROM ubuntu:23.04 as base

RUN apt update

FROM base as dependencies

RUN ./prereqs.sh

FROM dependencies as build

RUN ./build.sh

FROM build as test

RUN ./test.sh
