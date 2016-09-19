FROM ubuntu:14.04

MAINTAINER Mingliang Liu <liuml07@gmail.com>

RUN apt-get update
RUN apt-get install -qq -y make
RUN apt-get install -qq -y texlive-xetex
RUN apt-get install -qq -y python3-pip
RUN pip3 install beautifulsoup4 requests bibtexparser


ADD . google-scholar-citations
