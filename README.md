# google-scholar-citations
This program allows users to to retrieve all the citations from Google Scholar by specifying the Google Scholar page.

## Prerequisite
* Python 2.7.9+ or Python 3
  - [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
  - [requests](http://requests.readthedocs.io/en/latest/user/install/#install)
* Latex if you need to produce a final PDF report


## Basic Usage
Basic command line input is needed. A very basic usage will be:

```bash
$ python main.py https://scholar.google.com/citations?user=lqyGZpQAAAAJ
```

## More Options
```bash
$ python main.py [-h] [--request-interval REQUEST_INTERVAL] [--should-download]
               [--download-dir DOWNLOAD_DIR] [--citation-name CITATION_NAME]
               google_scholar_uri
```

### optional arguments:
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
