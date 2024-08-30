import sys
import os
from datetime import datetime

# ANSI escape sequences for colors
class Colors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def read_books_from_file(filepath):
    books = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                name, author, isbn, year = line.strip().split('/')
                books.append({
                    'name': name,
                    'author': author,
                    'isbn': isbn,
                    'year': int(year)
                })
        # Sorts books by ascending order
        books.sort(key=lambda x: x['year'])
    except FileNotFoundError:
        print(f"{Colors.FAIL}Error: The file {filepath} was not found.{Colors.ENDC}")
        return None
    except Exception as e:
        print(f"{Colors.FAIL}Error reading the file: {e}{Colors.ENDC}")
        return None
    return books

def write_books_to_file(filepath, books):
    try:
        with open(filepath, 'w') as file:
            for book in books:
                file.write(f"{book['name']}/{book['author']}/{book['isbn']}/{book['year']}\n")
    except Exception as e:
        print(f"{Colors.FAIL}Error writing to the file: {e}{Colors.ENDC}")

def book_exists(books, new_book):
    for book in books:
        if (book['name'].lower() == new_book['name'].lower() and
            book['author'].lower() == new_book['author'].lower() and
            book['isbn'] == new_book['isbn'] and
            book['year'] == new_book['year']):
            return True
    return False

def add_new_book(books):
    print("\n--- Adding a New Book ---")

    # Validate name input
    while True:
        name = input(Colors.OKCYAN + "Enter the name of the book: " + Colors.ENDC).strip().title()
        if name:
            break
        else:
            print(f"{Colors.FAIL}Book name cannot be empty. Please enter a valid book name.{Colors.ENDC}")

    # Validate author input
    while True:
        author = input(Colors.OKCYAN + "Enter the name of the author: " + Colors.ENDC).strip().title()
        if all(char.isalpha() or char.isspace() or char in "-'" for char in author) and author:
            break
        else:
            print(f"{Colors.FAIL}Author name should only contain letters, spaces, hyphens, or apostrophes.{Colors.ENDC}")
    
    # Validate ISBN input, with or without hyphens
    while True:
        isbn = input(Colors.OKCYAN + "Enter the 13-digit ISBN of the book: " + Colors.ENDC).strip()
        isbn_stripped = isbn.replace("-", "")  # Remove hyphens
        if len(isbn_stripped) == 13 and isbn_stripped.isdigit():
            break
        else:
            print(f"{Colors.FAIL}Invalid ISBN. Please enter a 13-digit number.{Colors.ENDC}")
    
    # Validate year input
    current_year = datetime.now().year
    while True:
        try:
            year = int(input(f"{Colors.OKCYAN}Enter the publishing year: {Colors.ENDC}").strip())
            if 0 <= year <= current_year:
                break
            else:
                print(f"{Colors.FAIL}Invalid year. Please enter a 4-digit year between 0 and {current_year}.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}Invalid input. Please enter a valid 4-digit year between 0 and {current_year}.{Colors.ENDC}")

    new_book = {'name': name, 'author': author, 'isbn': isbn_stripped, 'year': year}

    # Check if the book already exists in the db
    if book_exists(books, new_book):
        print(f"{Colors.WARNING}This book already exists in the database.{Colors.ENDC}")
        while True:
            add_new = input(f"{Colors.WARNING}Do you want to add a new book with different information? (Y/N): {Colors.ENDC}").strip().lower()
            if add_new == 'y':
                print("Please enter the new information.")
                return add_new_book(books)  # Restarts the process
            elif add_new == 'n':
                print("Book not added.")
                return
            else:
                print(f"{Colors.FAIL}Invalid input. Please enter 'Y' for yes or 'N' for no.{Colors.ENDC}")

    print("\nNew book details:")
    print(f"Name: {name}")
    print(f"Author: {author}")
    print(f"ISBN: {isbn_stripped}")
    print(f"Year: {year}")

    while True:
        confirm = input(Colors.WARNING + "Do you want to add this book to the database? (Y/N): " + Colors.ENDC).strip().lower()
        if confirm == 'y':
            books.append(new_book)
            # Sort books by publishing year in ascending order
            books.sort(key=lambda x: x['year'])
            print(f"{Colors.OKGREEN}Book added successfully!{Colors.ENDC}")
            break
        elif confirm == 'n':
            print("Book not added.")
            break
        else:
            print(f"{Colors.FAIL}Invalid input. Please enter 'y' for yes or 'n' for no.{Colors.ENDC}")

    print("Returning to the main menu...\n")

def print_books(books):
    print("\n--- Current Database Content (Sorted by Oldest First) ---\n")
    for book in books:
        print(f"Name: {book['name']}, Author: {book['author']}, ISBN: {book['isbn']}, Year: {book['year']}")
    print("\nReturning to the main menu...\n")

def main():
    if len(sys.argv) != 2:
        print("To access database, use: python my_library_db.py library.txt")
        return

    # Adjust file path to include C:\Testdata\lib-db
    base_directory = r"C:\Testdata\lib-db"
    filename = sys.argv[1]
    filepath = os.path.join(base_directory, filename)

    books = read_books_from_file(filepath)

    if books is None:
        return

    while True:
        print(Colors.HEADER + "\n--- Library Database Menu ---" + Colors.ENDC)
        print("1) Add new book")
        print("2) Print current database content")
        print("Q) Quit")
        choice = input(Colors.OKCYAN + "Choose an option: " + Colors.ENDC).strip().lower()

        if choice == '1':
            add_new_book(books)
            write_books_to_file(filepath, books)
        elif choice == '2':
            print_books(books)
        elif choice == 'q':
            confirm_exit = input(Colors.WARNING + "Are you sure you want to quit? (Y/N): " + Colors.ENDC).strip().lower()
            if confirm_exit == 'y':
                print(Colors.OKCYAN + "Exiting the program. Goodbye!"+ Colors.ENDC)
                break
            else:
                print("Returning to the main menu...\n")
        else:
            print(f"{Colors.FAIL}Invalid option, please choose again.{Colors.ENDC}")

if __name__ == "__main__":
    main()
