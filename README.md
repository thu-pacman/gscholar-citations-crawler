# Google Scholar Citations
Want to know who/which journal has cited your work and compile a list?

This program allows you to retrieve all the citations an author has garnered from other scholars via Google Scholar, to store them in a bib file, and optionally, to download the publicly available PDF files associated with those citations.

## Prerequisite
* Python 2.7.9+ or Python 3
  - [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
  - [requests](http://requests.readthedocs.io/en/latest/user/install/#install)
  - [bibtexparser](https://bibtexparser.readthedocs.io/en/v0.6.2/install.html)
* Latex if you need to produce a final PDF report

## Download
To download, either directly [download the zip file](https://github.com/shiqiezi/google-scholar-citations/archive/master.zip), or clone the git repository via command line with:
```bash
$ git clone https://github.com/shiqiezi/google-scholar-citations
```

## Basic Usage
Basic command line operation is needed. A very basic usage with defaults will be:

```bash
$ python main.py https://scholar.google.com/citations?user=lqyGZpQAAAAJ
```

## More Options
```bash
$ python main.py [-h] [--request-interval REQUEST_INTERVAL] [--should-download]
               [--download-dir DOWNLOAD_DIR] [--citation-name CITATION_NAME]
               google_scholar_uri
```

### optional arguments explained:
```bash
  --request-interval REQUEST_INTERVAL
                        # Interval (in seconds) between requests to google scholar
  --should-download     # Download PS/PDF files of all citations iff True
  --download-dir DOWNLOAD_DIR
                        # Directory for downloaded citations PDF files
  --citation-name CITATION_NAME
                        # File name for all your citations in BibTex format
```
### positional argument:
```bash
  google_scholar_uri    # Your google scholar homepage
```

###Example
```bash
$ python main.py --request-interval=50 --should-download https://scholar.google.com/citations?user=lqyGZpQAAAAJ
```

## Getting Help
```bash
$ python main.py -h # show this help message and exit
```

## Avoid Too Many Requests
Crawl the web resposibly. We suggest that users set a large number for the --request-interval. Requesting too frequently may result in a block from Google.

## History
*18-Sep-2016*: Enabled a number of command line options, updated README
