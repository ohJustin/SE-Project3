# Reddit Website Scraper ....
# *e.g link* https://www.reddit.com/r/funny/comments/16brnzb/self_aware/
import sys
import requests


# NOTE: CLEAR THE 'content.txt' FILE TO SEE THE PROGRAM EXTRACT FROM AN EMPTY STATE.
# 'To Run Program -> python .\main.py *URL*
#    ---->          python  your_program.py  URL-Link
# URL = sys.argv[1]

def raw_extraction(url_to_extract):
    file = open("rawdata,txt", "w")
    page_to_scrape = requests.get(url_to_extract)
    print("Page Scrape started...")

    if not page_to_scrape:
        print("Error while extracting page...")
    else:
        file.write(page_to_scrape.text)
        print("Page extracted...")

    file.close()
    print("Scraper Ran ...")
