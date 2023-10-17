import sys
from module_1 import raw_extraction
from module_2 import data_processor

if __name__ == "__main__":
    #command given from argument... > python3 run.py URL
    url_from_sys = sys.argv[1]

    #Extract data raw
    data = raw_extraction(url_from_sys)

    if(data):
        data_processor(data, output_file="Data/processed/comments.txt")