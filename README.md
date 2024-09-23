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
* `fetchincidents(pdf)`
  * Parameters: Path to the PDF file.
  * Process: Extracts the text from the PDF using PdfReader, concatenating all pages' text into a single string.
  * Returns: A string of raw incident report data.

* `extractincidents(data)`
  * Parameters: Raw text data from the PDF.
  * Process:Splits the data into lines and processes it to extract relevant fields, handling multi-line addresses.
  * Returns: A list of rows, where each row represents a structured incident report.

* `createdb()`
  * Process: Creates an SQLite database with a table named incidents. The table contains the columns for storing incident details: incident_time, incident_number, incident_location, nature, and incident_ori.
  * Returns: None.

* `populatedb(separated_data)`
  * Parameters: List of extracted incidents data.
  * Process: Inserts each row into the SQLite database incidents table.
  * Returns: None.

## Database Development
The database is developed using SQLite and includes a single table, incidents, with the following columns:
* `incident_time` (TEXT)
* `incident_number` (TEXT)
* `incident_location` (TEXT)
* `nature` (TEXT)
* `incident_ori` (TEXT)

The database is created with the `createdb()` function and populated by the `populatedb()` function.
## Bugs and Assumptions
* Multi-line addresses and fields are assumed to belong to the same incident and are concatenated as part of the parsing logic.
* Some incidents may not follow the expected pattern, which could lead to incomplete or incorrect rows being added to the database.
* Assumes the PDF file structure remains consistent throughout the document.
