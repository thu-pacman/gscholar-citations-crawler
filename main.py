#!/usr/bin/env python

import sys
import math
import urllib2
import time
from BeautifulSoup import BeautifulSoup
import logging
import HTMLParser

import myconfig

REQUEST_HEADERS = {"User-Agent":"Innocent Browser", "Accept-Charset":"UTF-8,*;q=0.5"}
SLEEP_INTERVAL = 10 # sleep in seconds before next request
CITATION_FILENAME = "citation.txt"

citation_num = 0
download_num = 0

html_parser = HTMLParser.HTMLParser()

def get_all_citations():
    total_citations_num = get_total_citations_num()
    papers_per_page = 20
    paper_uri_template = myconfig.google_scholar_uri + "&cstart=%d&pagesize=%d"
    for c in range(0, int(math.ceil(total_citations_num * 1.0 / papers_per_page))):
        paper_uri = paper_uri_template % (papers_per_page * c, papers_per_page)
        logging.info("Processing GOOGLE_SCHOLAR_URI: " + paper_uri)
        soup = create_soup_by_url(paper_uri)
        paper_records = soup("tr", {"class":'gsc_a_tr'})
        for p in paper_records:
            paper_title = p.find('a', {"class":"gsc_a_at"}).getText()
            logging.info("Processing paper: " + paper_title)
            citations_anchor = p.find('a', {"class":'gsc_a_ac'})
            if citations_anchor['href']:
                with open(CITATION_FILENAME, "a+") as f:
                    f.write("# %s\n" % paper_title)
                get_citations_by_paper(citations_anchor['href'], int(citations_anchor.getText()))
            else:
                logging.warn("Current paper has not been cited.")

def get_total_citations_num():
    """
    Get the total citation number from user's google scholar homepage
    """
    soup = create_soup_by_url(myconfig.google_scholar_uri)
    total_citations_num = int(soup("td", {"class":"gsc_rsb_std"})[0].getText())
    logging.info("Total citations number: %d" % total_citations_num)
    return total_citations_num

def get_citations_by_paper(citations_uri, count):
    logging.debug("citations_uri: %s count: %d" % (citations_uri, count))
    citations_uri_template = citations_uri + "&start=%d"
    for c in range(0, int(math.ceil(count / 10.0))):
        curr_citations_uri = citations_uri_template % (c * 10)
        logging.debug("Processing citations_uri: " + curr_citations_uri)
        soup = create_soup_by_url(curr_citations_uri)
        for citation_record in soup('div', {"class":"gs_r"}):
            save_citation(citation_record)

def save_citation(citation_record):
    CITE_DETAIL_URL_TEMPLATE = "https://scholar.google.com/scholar?q=info:%(id)s:scholar.google.com/&output=cite"
    cite_anchor = citation_record.find('a', {'class' : 'gs_nph', 'href' : '#', "role":"button"})
    if not cite_anchor:
        return
    citation_id = cite_anchor['onclick'].split(',')[1][1:-1]
    cite_detail_url = CITE_DETAIL_URL_TEMPLATE % {"id" : citation_id}
    logging.info("Getting formated cite from " + cite_detail_url)
    soup = create_soup_by_url(cite_detail_url)
    global html_parser
    full_cite = html_parser.unescape(soup.find("div", {"id":"gs_cit0"}).text)
    global citation_num
    citation_num = citation_num + 1
    with open(CITATION_FILENAME, "a+") as f:
        f.write("[%d] %s\n" % (citation_num, full_cite))
    if myconfig.should_download:
        pdf_div = citation_record.find('div', {"class":"gs_ggs gs_fl"})
        if pdf_div:
            download_pdf(pdf_div.a['href'])

def download_pdf(pdf_uri):
    global citation_num, download_num
    pdf = None
    try:
        pdf = urllib2.urlopen(pdf_uri)
        with open("%d.pdf" % citation_num, "wb") as mypdf:
            mypdf.write(pdf.read())
        download_num = download_num + 1
        logging.info("Downloaded citation [%d] from link %s " % (citation_num, pdf_uri))
    except urllib2.URLError as err:
        logging.error("Can't download link: " + pdf_uri + " Error: " + str(err.reason))
    finally:
        if pdf:
            pdf.close()


def create_soup_by_url(page_url):
    req = urllib2.Request(page_url, headers = REQUEST_HEADERS)
    page = None
    try:
        time.sleep(SLEEP_INTERVAL)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page)
        if soup.h1 and soup.h1.text and soup.h1.text == "Please show you&#39;re not a robot":
            raise Exception("You need to verify manually that you're not a robot.")
        return soup
    except Exception as err:
        logging.error("Can't open link: " + page_url + " Error: " + str(err))
        sys.exit(1)
    finally:
        if page:
            page.close()

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    logging.basicConfig(level = logging.DEBUG)
    get_all_citations()
    logging.info("Found %d citations and download %d files" % (citation_num, download_num))

if __name__ == "__main__":
    sys.exit(main())
