FROM ubuntu

MAINTAINER Mingliang Liu <liuml07@gmail.com>

RUN apt-get update
RUN apt-get install -qq -y python-beautifulsoup

ADD . google-scholar-citations
