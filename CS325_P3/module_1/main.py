# Reddit Website Scraper ....
# *e.g link* https://www.reddit.com/r/funny/comments/16brnzb/self_aware/
import sys
import requests

#NOTE: CLEAR THE 'content.txt' FILE TO SEE THE PROGRAM EXTRACT FROM AN EMPTY STATE.
#'To Run Program -> python .\main.py *URL*
#    ---->          python  your_program.py  URL-Link
URL = sys.argv[1]

file = open("content.txt", "w")
page_to_scrape = requests.get(URL)
print("Page Scrape started...")

file.write(page_to_scrape.text)
print("Page extracted...")


file.close()
print("Scraper Ran ...")
