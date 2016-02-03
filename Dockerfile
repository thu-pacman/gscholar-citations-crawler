FROM ubuntu:14.04

MAINTAINER Mingliang Liu <liuml07@gmail.com>

RUN apt-get update
RUN apt-get install -qq -y python3-bs4 python3-requests
RUN apt-get install -qq -y texlive-xetex
RUN apt-get install -qq -y make

ADD . google-scholar-citations
