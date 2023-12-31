import sys
from module_1.main import raw_extraction
from module_2.main import data_processor
import module_2
#This program utilizes its imports to produce raw / processed data from a URL.
if __name__ == "__main__":
    #command given from argument... > python3 run.py URL
    url_from_sys = sys.argv[1]

    #Extract data raw
    data = raw_extraction(url_from_sys)

    if data:
        processed_signal = data_processor(data)
        if(processed_signal):
            print("Processing complete")
        else:
            print("Processing failed")