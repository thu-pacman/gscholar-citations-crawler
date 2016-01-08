#!/usr/bin/env python

import sys
import math
import urllib2
import time
from BeautifulSoup import BeautifulSoup
import logging

import myconfig

REQUEST_HEADERS = {"User-Agent":"Innocent Browser", "Accept-Charset":"UTF-8,*;q=0.5"}
SLEEP_INTERVAL = 10 # sleep in seconds before next request

citation_num = 0
download_num = 0

def get_all_citations():
    logging.debug("Processing GOOGLE_SCHOLAR_URI: " + myconfig.google_scholar_uri)
    req = urllib2.Request(myconfig.google_scholar_uri, headers=REQUEST_HEADERS)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    paper_records = soup("tr", {"class":'gsc_a_tr'})
    for p in paper_records:
        logging.info("Processing paper: " + p.find('a', {"class":"gsc_a_at"}).getText())
        citations_anchor = p.find('a', {"class":'gsc_a_ac'})
        if citations_anchor['href']:
            get_citations_by_paper(citations_anchor['href'], int(citations_anchor.getText()))
        else:
            logging.info("Current paper has not been cited.")

def get_citations_by_paper(citations_uri, count):
    logging.debug("Processing citations_uri: " + citations_uri)
    citations_uri_template = citations_uri + "&start=%d"
    for c in range(0, int(math.ceil(count / 10.0))):
        curr_citations_uri = citations_uri_template % (c * 10)
        logging.debug("Processing citations_uri:" + curr_citations_uri)
        req = urllib2.Request(curr_citations_uri, headers=REQUEST_HEADERS)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page)
        for citation_record in soup('div', {"class":"gs_r"}):
            save_citation(citation_record)
        time.sleep(SLEEP_INTERVAL)

def save_citation(citation_record):
    global citation_num, download_num
    citation_info = citation_record.find('div', {"class":"gs_ri"})
    title = citation_info.h3.a.renderContents()
    citation_num = citation_num + 1
    with open("citation.txt", "a+") as f:
        f.write("[%d]" % citation_num + " " + title + '\n')
    if myconfig.should_download:
        pdf_uri = citation_record.find('div', {"class":"gs_ggs gs_fl"}).a['href']
        if pdf_uri:
            pdf = urllib2.urlopen(pdf_uri)
            with open("%d.pdf" % citation_num, "wb") as mypdf:
                mypdf.write(pdf.read())
            download_num = download_num + 1

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    logging.basicConfig(filename = 'citation.log', filemode = 'w+', level = logging.DEBUG)
    get_all_citations()
    logging.info("Found %d citations and download %d files" % (citation_num, download_num))

if __name__ == "__main__":
    sys.exit(main())
