import os
import pandas as pd
import re
import math
import csv

SID = 'CSID'
TSP = 'Total Score (%)'
OUT_FILE = 'output.csv'

def get_files():
    return [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.xlsx')]

def parse_data(files):
    data = {}
    for file in files:
        lec = file.split()[0]

        df = pd.read_excel(file, header=5, names=[SID, TSP], usecols='C,D', skipfooter=3)

        for _, row in df.iterrows():
            id = row[SID]
            if id is '-':
                continue

            sc = row[TSP]
            if sc is '-':
                sc = 0

            if id not in data:
                data[id] = {"CSID": id}

            data[id][lec] = sc

    return data

def output_data(data):
    csv_data = []
    for key in data:
        csv_data += [data[key]]

    csv_columns = csv_data[0].keys()
    
    try:
        with open(OUT_FILE, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
            writer.writeheader()
            for data in csv_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    return

if __name__ == '__main__':
    print('Starting program')
    files = get_files()
    count = len(files)
    
    if count < 1:
        print('Found no data, terminating program')
        exit()
    else:
        print('Found ' + str(count) + ' files, beginning to parse')

    data = parse_data(files)
    print('Found data for ' + str(len(data)) + ' students, printing to ' + OUT_FILE)

    output_data(data)

    print('File printed, finished program')


