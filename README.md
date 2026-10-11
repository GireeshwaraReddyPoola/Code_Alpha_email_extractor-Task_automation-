EMAIL EXTRACTOR - TASK AUTOMATION WITH PYTHON SCRIPTS

ABOUT THE PROJECT
---------------------------------------------------------------------
This script automates a simple, repetitive task of finding all email
addresses in a text file and saving them in a separate file.

Doing this manually takes a lot of time to review the entire file
copying all the addresses, whereas the script does it in a fraction of
the time, removing duplicates and sorting them.
Concepts used: os, re (regular expressions), file handling,
functions, error handling (try/except).
REQUIREMENTS
---------------------------------------------------------------------
- Python 3.8 or newer

Check with: python --version
- No extra libraries are needed (uses only built-in modules)
PROJECT STRUCTURE
---------------------------------------------------------------------
Task 3-Task automation/
|-- email_extractor.py  (the script)
|-- sample_input.txt   (input file with test data)
|-- README.txt      (this file)
|-- output/        (created automatically)
|-- emails_found.txt  (the result)
Important: email_extractor.py and sample_input.txt must be in the
SAME folder.
HOW TO RUN
---------------------------------------------------------------------
Option 1 - VS Code:
Open email_extractor.py and click the Run button.
Option 2 - Terminal:
Open a terminal in the project folder and run:
python email_extractor.py
HOW IT WORKS
---------------------------------------------------------------------
1. Opens sample_input.txt and reads all the text.
2. Uses a regular expression to find every email pattern:
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
3. Converts emails to lowercase, removes duplicates (set) and
sorts them alphabetically.
4. Creates the output folder if it does not exist.
5. Writes one email per line to output/emails_found.txt.
6. Prints how many emails were found and where they were saved.
SAMPLE OUTPUT
---------------------------------------------------------------------
Found 4 unique email(s).
- help@my-site.org
- jane_smith@company.co.in
- john.doe@example.com
- sales+2026@my-site.org
Saved to output/emails_found.txt
The sample file contains invalid entries (hello@, @nouser.com,
plainaddress) and one duplicate (john.doe@example.com); the script
ignores the invalid ones and keeps the duplicate only once.
USING YOUR OWN FILE
---------------------------------------------------------------------
Put your .txt file in the same folder and change this line in main():
input_path = os.path.join(BASE_DIR, "sample_input.txt")
with your file name, for example "my_notes.txt".
ERROR HANDLING
---------------------------------------------------------------------
- Input file missing -> prints a clear message instead of crashing
- No emails found   -> prints "No email addresses found."
- Output folder missing -> created automatically
- Special characters -> files are read/written with UTF-8 encoding
TROUBLESHOOTING
---------------------------------------------------------------------
Problem : "Input file not found: ...sample_input.txt"
Fix   : - Make sure sample_input.txt is in the same folder as the
script.
- On Windows, check the file is not named
sample_input.txt.txt (hidden extension). Rename it if so.
LIMITATIONS
---------------------------------------------------------------------
- The pattern is practical but not a complete email validator, so
very unusual addresses may be missed.
- Only plain text files are supported (not PDF or Word).
POSSIBLE IMPROVEMENTS
---------------------------------------------------------------------
- Take the input file name from the command line (argparse)
- Show how many emails were found per domain
- Also save the results to a .csv file
- Support reading several files at once
AUTHOR
---------------------------------------------------------------------
Name  : Gireeshwarareddy
Project: Python Internship - Task Automation with Python Scripts