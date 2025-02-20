from project0.main import downloaddata, fetchincidents, extractincidents, createdb, populatedb, status
import os
import sqlite3

def test_download_data():
    downloaddata("https://www.normanok.gov/sites/default/files/documents/2024-08/2024-08-01_daily_incident_summary.pdf")
    assert os.path.exists("resources/incident1.pdf")    

def test_fetch_incidents():
    assert os.path.exists("resources/incident1.pdf")
    data = fetchincidents("resources/incident1.pdf")
    assert data is not None
        
def test_extract_incidents():
    assert os.path.exists("resources/incident1.pdf")
    data = fetchincidents("resources/incident1.pdf")
    rows = extractincidents(data)
    assert len(rows[0]) == 5

def test_create_db():
    createdb()
    assert os.path.exists("resources/normanpd.db")

def test_populate_db():
    data = fetchincidents("resources/incident1.pdf")
    separated_data = extractincidents(data)
    createdb()
    populatedb(separated_data)
    conn = sqlite3.connect("resources/normanpd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents")
    results = cursor.fetchall()
    assert len(results) != 0
    conn.close()

def test_status():
    data = fetchincidents("resources/incident1.pdf")
    separated_data = extractincidents(data)
    createdb()
    
    populatedb(separated_data)
    try_data = status()
    
    data = ''
    with open("resources/status.txt", "r") as file:
        lines = file.readlines()
    
    for i in lines:
        data += i
    assert data==try_data
    