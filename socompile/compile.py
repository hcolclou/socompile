import os
import pandas as pd
import re
import math
import csv
import ntpath

SID = 'ID'
TSP = 'Total Score (%)'
OUT_FILE = 'output.csv'

def get_files(dir):
    """
    get files from given directory
    
    Parameters
    ----------
    dir: str
       path to directory with excel files

    Returns
    -------
    list of file names
    """
    return [os.path.join(dir, f) for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f)) and f.endswith('.xlsx')]

def parse_data(files, basename):
    """
    parse all given files for student data
    
    Parameters
    ----------
    files: list of str
        paths to xlsx file
    basename: str
        path to director of files

    Returns
    -------
    dict of student data
    """
    data = {}
    for file in files:
        ntpath.basename(basename)
        _, tail = ntpath.split(file)
        lec = tail.split()[0]

        df = pd.read_excel(file, header=5, names=[SID, TSP], usecols='C,D', skipfooter=3)

        for _, row in df.iterrows():
            id = row[SID]
            if id is '-':
                continue

            sc = row[TSP]
            if sc is '-':
                sc = 0

            if id not in data:
                data[id] = {SID: id}

            data[id][lec] = sc

    return data

def output_data(data, out_file):
    """
    print output data to csv
    
    Parameters
    ----------
    files: dict
        dict of student data
    out_file: str
        path to file to write to

    Returns
    -------
    None
    """
    csv_data = []
    for key in data:
        csv_data += [data[key]]

    csv_columns = csv_data[0].keys()
    
    try:
        with open(out_file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
            writer.writeheader()
            for data in csv_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    return

def run(dir, out_file):
    print('Starting program')
    files = get_files(dir)
    count = len(files)
    
    if count < 1:
        print('Found no data, terminating program')
        exit()
    else:
        print('Found ' + str(count) + ' files, beginning to parse')

    data = parse_data(files, dir)
    print('Found data for ' + str(len(data)) + ' students, printing to ' + out_file)

    output_data(data, out_file)

    print('File printed, finished program')


