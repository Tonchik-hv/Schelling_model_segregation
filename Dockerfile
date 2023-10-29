FROM ubuntu:23.04 as base

RUN apt update
RUN apt install git -y
RUN git clone https://github.com/Tonchik-hv/Schelling_model_segregation.git
RUN cd ./Schelling_model_segregation
