FROM ubuntu:14.04

MAINTAINER Mingliang Liu <liuml07@gmail.com>

RUN apt-get update
RUN apt-get install -qq -y python-bs4 python-requests
RUN apt-get install -qq -y texlive-xetex
RUN apt-get install -qq -y make

ADD . google-scholar-citations
