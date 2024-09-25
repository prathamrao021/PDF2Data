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
pipenv run python project0/main.py --incidents <Incident_URL>
```
Replace `Incident_URL` with the actual URL of the incident summary PDF.
![https://github.com/user-attachments/assets/3a9f99db-3b96-495c-94d2-75bc48b7c84a](https://github.com/prathamrao021/cis6930fa24-project0/issues/1#issue-2548928125)

## How to Run Tests
To run test, execute the main.py code first in order to generate the file in dedicated location.
To run the test suite with `pytest`, execute the following command:
```bash
pipenv run python -m pytest
```

## Functions
`main.py`
* `downloaddata(url)`
  * Parameters: URL to the PDF file.
  * Process: Downloads the incident PDF from the provided URL and saves it locally as `incident1.pdf`.
  * Returns: The name of the saved file `(incident1.pdf)`.

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

## Test Functions
`test_main.py`
* `test_downloaddata()`
  * Process: Tests the `downloaddata` function by providing a sample URL and verifying that the file is downloaded and saved as `incident1.pdf`.
  * Returns: None.

* `test_fetchincidents()`
  * Process: Tests the `fetchincidents` function by providing a sample PDF file and verifying that the extracted text matches the expected output.
  * Returns: None.

* `test_extractincidents()`
  * Process: Tests the `extractincidents` function by providing sample raw text data and verifying that the extracted rows match the expected structured data.
  * Returns: None.

* `test_createdb()`
  * Process: Tests the `createdb` function by verifying that the SQLite database and the incidents table are created successfully.
  * Returns: None.

* `test_populatedb()`
  * Process: Tests the `populatedb` function by providing sample extracted incidents data and verifying that the data is inserted into the SQLite database correctly.
  * Returns: None.
  
## Database Development
The database `tutorial.db` is developed using SQLite and includes a single table, incidents, with the following columns:
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
