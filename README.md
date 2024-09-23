# CIS6930FA24 - Project 0

**Name:** Pratham Rao

## Project Description
This project is focused on processing PDF data for incident reports, extracting relevant fields such as date/time, incident number, location, nature, and incident ORI. The data is then parsed, cleaned, and stored in an SQLite database for further analysis or querying. The project demonstrates how to handle structured and semi-structured data, including multi-line entries in the PDF.

## How to Install
To install the required dependencies, use `pipenv`:

```bash
pipenv install
```

## How to Run
```bash
pipenv run python main.py
```
![video](video)


## Functions
`main.py`
fetchincidents(pdf)
Parameters: Path to the PDF file.
Process: Extracts the text from the PDF using PdfReader, concatenating all pages' text into a single string.
Returns: A string of raw incident report data.

extractincidents(data)
Parameters: Raw text data from the PDF.
Process:

Splits the text into lines.
Removes header/footer lines and processes incident lines by splitting fields.
Handles multi-line fields like addresses. Returns: A list of rows, each representing a structured incident report (date/time, incident number, location, etc.).
createdb()
Process:

Creates an SQLite database with a table named incidents.
The table contains the columns for storing incident details: incident_time, incident_number, incident_location, nature, and incident_ori.
Returns: None.
populatedb(separated_data)
Parameters: List of extracted incidents data.
Process:

Iterates over the list of incident rows.
Inserts each row into the SQLite database incidents table.
Returns: None.

## Database Development
...

## Bugs and Assumptions
...
