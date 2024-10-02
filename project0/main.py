import urllib.request
from pypdf import PdfReader
import pandas as pd
import re
import sqlite3
import argparse
import os
def downloaddata(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    with open(f'resources/incident1.pdf', 'wb') as file:
        file.write(data)
    return 'incident1.pdf'

def fetchincidents(pdf):
    reader = PdfReader(pdf)
    data = ''
    for page in reader.pages:
        data = data + "\n" + page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
    # with open('docs/test.txt','w') as file:
    #     file.write(data)
    return data


def extractincidents(data):
    
    lines = (data.split("\n"))[3:-1]
    rows = []
    # for line in lines:
    #     split_line = []
    #     for field in line.split("          "):
    #         if field != "":
    #             split_line.append(field.strip())
    #     rows.append(split_line)
    # return rows
    temp_row = []
    for line in lines:
        split_line = [field.strip() for field in line.split("          ") if field.strip()]

        if len(split_line) < 5:
            if len(temp_row) > 0:
                temp_row[2] += " " + split_line[0]
        else:
            if len(temp_row) == 5:
                rows.append(temp_row)
            temp_row = split_line  
    
    if len(temp_row) == 5:
        rows.append(temp_row)
    
    return rows
    
    
def createdb():
    if os.path.exists("resources/normanpd.db"):
        os.remove("resources/normanpd.db")
    conn = sqlite3.connect("resources/normanpd.db")
    
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS incidents (incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT)")
    
    conn.commit()
    conn.close()


def populatedb(separated_data):
    conn = sqlite3.connect("resources/normanpd.db")
    
    cursor = conn.cursor()
    
    cursor.executemany("INSERT INTO incidents VALUES(?, ?, ?, ?, ?)", separated_data)
    conn.commit()
    conn.close()

def status():
    conn = sqlite3.connect("resources/normanpd.db")
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT nature, count(nature) FROM incidents GROUP BY nature ORDER BY nature ASC")
    printables = cursor.fetchall()
    data = ''
    with open("resources/status.txt", "w") as file:
        for i,v in enumerate(printables):
            if v[0] == "Nature":
                continue
            if i != len(printables) - 1:
                file.write(f"{v[0]}|{v[1]}\n")
                data += f"{v[0]}|{v[1]}\n"
            else:
                file.write(f"{v[0]}|{v[1]}")
                data += f"{v[0]}|{v[1]}"
    conn.close()
    print(data)
    return data

if __name__ == "__main__":
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, help="Incident summary url.")
    args = parser.parse_args()
    
    filename = downloaddata(args.incidents)
    data = fetchincidents("resources/incident1.pdf")
    separated_data = extractincidents(data)
    createdb()
    populatedb(separated_data[1:])
    status()
    
    