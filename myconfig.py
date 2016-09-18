#!/usr/bin/env python

# This is your google scholar homepage. Add all your papers to your page.
google_scholar_uri = "https://scholar.google.com/citations?user=NMS69lQAAAAJ"

# This controls the interval (in seconds) between requests to google scholar.
# Not that a small interval will get this script banned by google
request_interval = 100

# Download PS/PDF files of all citations iff True
should_download = True
# Directory for downloaded citations PS/PDF files
download_dir = "pdf"
