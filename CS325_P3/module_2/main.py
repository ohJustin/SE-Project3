from bs4 import BeautifulSoup
import sys
import requests


#This module expects data to process to be returned within the parameters. It takes this text, uses line 16 to parse and writes the text into the comments.txt file.
def data_processor(data_process):
    try:
        print("Processing pt.1 started")
        file_name = "../CS325_P3/Data/processed/comments.txt"

        # Soup instantiation
        soup = BeautifulSoup(data_process, 'lxml')

        bot_trigger = False
        comments = soup.find_all('div', class_=lambda x: x and x.startswith('thing id-t1_'))

        # Open the file to write comments
        with open(file_name, 'w', encoding='utf-8', errors = 'replace') as file:
            print("Processing started...")

            for readcomments in comments:
                text = readcomments.find('div', class_='md').get_text()
                # Find bot comments, then extract Reddit comments.
                if "I am a bot, and this action was performed automatically." in text:
                    bot_trigger = True
                    continue

                if bot_trigger:
                    file.write(text + "\n")  # Write each comment on a new line
                    print("Extraction/process success")

        #print("Process finished")
    except Exception as e:
        print("err whilst processing data:", e)
    return 1
