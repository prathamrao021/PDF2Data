import urllib.request
from pypdf import PdfReader
import pandas as pd
import re
import sqlite3
def fetchincidents(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    print(data)

def extractincidents(pdf):
    page = PdfReader(pdf).pages[0]
    data = page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
    
    
    lines = (data.split("\n"))[3:]
    columns = ['Date / Time', 'Incident Number', 'Location', 'Nature', 'Incident ORI']
    rows = []
    for line in lines:
        split_line = []
        for field in line.split("          "):
            if field != "":
                split_line.append(field.strip())
        rows.append(split_line)
    
    print(rows)
    
    
    conn = sqlite3.connect("docs/tutorial.db")
    
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS incidents (incident_time TEXT, incident_number TEXT, incident_location TEXT, nature TEXT, incident_ori TEXT)")
    
    
    cursor.executemany("INSERT INTO incidents VALUES(?, ?, ?, ?, ?)", rows)
    
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    # fetchincidents("https://www.normanok.gov/sites/default/files/documents/2024-08/2024-08-02_daily_arrest_summary.pdf")
    extractincidents("docs/Incidetnt1.pdf")