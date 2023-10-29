FROM ubuntu:23.04 as base

RUN apt update
RUN apt install git -y


COPY .. ./Schelling_model_segregation/
# UNCOMMENT LATER
#RUN git clone https://github.com/Tonchik-hv/Schelling_model_segregation.git


RUN cd ./Schelling_model_segregation; chmod +x prereqs.sh build.sh test.sh

FROM base as dependencies

RUN ./Schelling_model_segregation/prereqs.sh

FROM dependencies as build
WORKDIR ./Schelling_model_segregation

RUN ./build.sh

FROM build as test

RUN ./test.sh

FROM test as entry

RUN ./run.sh 16 0.25
ENTRYPOINT ["bash"]
