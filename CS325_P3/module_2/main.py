from bs4 import BeautifulSoup
import sys
import requests



# Grab txt file from user.
# txtfile = sys.argv[1]

def data_processor(data_to_process):
    try:
        file_name = "comments.txt"
        # open file to write comments to.
        file = open("../Data/processed/comments.txt", "w", encoding='utf-8')

        # opening txtfile to read from
        with open(file_name, 'r', encoding='utf-8') as readfile:
            content = readfile.read()

            # soup instantiation
            soup = BeautifulSoup(content, 'lxml')

            bot_trigger = False
            comments = soup.find_all('div', class_=lambda x: x and x.startswith('thing id-t1_'))

        for readcomments in comments:
            text = readcomments.find('div', class_='md').get_text()
            #Finds bot comments, then finally starts the parsing/extraction of reddit comments which should work for all sites.
            if "I am a bot, and this action was performed automatically." in text:
                bot_trigger = True
                continue

            if bot_trigger:
                file.write(str(text))

        file.close()
    except Exception as E:
        print("error extracting...", E)


