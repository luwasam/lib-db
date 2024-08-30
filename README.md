# Library Database Program

This Python program allows you to manage a library database stored in a text file. 
Program enables you to add new books, view the current database content, and ensure that all entries are formatted consistently. 
The database is stored in a file with each book's details recorded on a new line.

## Features

- **Add New Books**: Input details for a new book, including its name, author, ISBN, and publication year.
- **View Database**: Display all books currently stored in the database, sorted by publication year (oldest to newest).
- **Data Validation**: Ensures that book entries are correctly formatted, with no leading or trailing spaces, and that each field contains valid data.
- **Duplicate Detection**: Checks if a book with the same details already exists in the database before adding a new entry.

## Prerequisites

- Python 3.x installed on your system.

**Getting Started**
1) Clone the Repository for example to folder C:\Testdata\:<br/>
cd C:\Testdata<br/>
git clone https://github.com/luwasam/lib-db.git<br/>

or

2) folder of your choosing, but make sure you change the path<br/>
from line 143 from the my_library_db.py file to:<br/>
base_directory = r"C:\YOUROWNFOLDER\lib-db" 

## Project Structure

For example, file path:
C:\Testdata\lib-db

### Which includes
### Text file where the book database is stored
library.txt         

### Python file
my_library_db.py

### Set Up the library.txt File:
Create a library.txt file in the C:\Testdata\lib-db directory if it does not already exist.<br/>
The file should be formatted with one book per line, using the following format:<br/>
Book Name/Author Name/ISBN/Year<br/>
Make sure the library.txt file is located in i.e. C:\Testdata\lib-db directory without white spaces.

**Run the Program:**

Use the following command to run the program:<br/>
python my_library_db.py library.txt <br/>
![image](https://github.com/user-attachments/assets/20ee724f-31fb-488a-a45b-ae3ffe1b88e6) <br/>
![image](https://github.com/user-attachments/assets/bcb28e14-d381-4376-b4e3-b71af5774960)
