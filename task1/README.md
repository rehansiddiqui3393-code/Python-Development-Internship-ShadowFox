Python Development Internship - ShadowFox

Submission of all tasks for the Python Development Internship at ShadowFox.

Name: MOHD REHAN SIDDIQUI Email: rehansiddiqui@gmail.com

Project Structure
Python-Development-Internship/
├── README.md
├── requirements.txt
├── Task1_Beginner/
│   ├── 01_variables.py
│   ├── 02_numbers.py
│   ├── 03_list.py
│   ├── 04_if_condition.py
│   ├── 05_for_loop.py
│   ├── 06_dictionary.py
│   ├── 07_file_handling.py
│   ├── 08_classes_objects.py
│   ├── 09_inheritance.py
│   └── student_marks.csv
├── Task2_Intermediate/
│   ├── web_scraper.py
│   └── hangman.py
└── Task3_Advanced/
    ├── cricket_fielding_analysis.py
    ├── fielding_data.csv
    ├── Cricket_Fielding_Analysis.xlsx
    ├── performance_matrix.csv
    ├── analysis_report.md
    └── charts/
Task 1 - Beginner Level

Nine programs that cover the Python basics.

File	Topic	What it does
01_variables.py	Variables	Stores 22/7 and checks its type, explains why for cannot be a variable name, calculates Simple Interest
02_numbers.py	Numbers	Uses format() for octal, finds the pond area and water volume, calculates speed
03_list.py	List	Adds, moves, replaces and sorts the Justice League list
04_if_condition.py	If Condition	BMI category, city to country lookup, same-country check
05_for_loop.py	For Loop	Dice roll statistics and a jumping jacks workout program
06_dictionary.py	Dictionary	Name-length tuples and trip expense comparison
07_file_handling.py	File Handling	Reads a CSV, adds total and average marks, writes new files
08_classes_objects.py	Classes and Objects	Avenger class with get_info() and is_leader()
09_inheritance.py	Inheritance	MobilePhone base class with Apple and Samsung child classes using super()

Run: python Task1_Beginner/01_variables.py (Run 07_file_handling.py from inside the Task1_Beginner folder so it finds student_marks.csv.)

Task 2 - Intermediate Level
1. Web Scraper (web_scraper.py)
Scrapes quotes, authors and tags from quotes.toscrape.com using Requests and Beautiful Soup.
Follows the "Next" button across several pages and saves the data to quotes.csv.
Prints a summary (total quotes, unique authors, most quoted author).
2. Hangman (hangman.py)
Word guessing game with an ASCII drawing that builds up with wrong guesses.
Random words from three categories: Programming, Animals and Countries.
Type hint to get a clue (costs one life).
Handles invalid and repeated input, and lets you play again.

Run:

bash
python Task2_Intermediate/web_scraper.py
python Task2_Intermediate/hangman.py

Task 3 - Advanced Level: Cricket Fielding Analysis

Fielding performance analysis of three players from a T20 innings.

Performance Score formula

PS = (CP x WCP) + (GT x WGT) + (C x WC) + (DC x WDC) + (ST x WST)
     + (RO x WRO) + (MRO x WMRO) + (DH x WDH) + RS
Metric	Weight
Clean Pick (CP)	+1
Good Throw (GT)	+1
Catch (C)	+3
Dropped Catch (DC)	-3
Stumping (ST)	+3
Run Out (RO)	+3
Missed Run Out (MRO)	-2
Direct Hit (DH)	+2
Runs Saved (RS)	added as it is

What is included

fielding_data.csv - ball-by-ball fielding data (Match No., Innings, Team, Player Name, BallCount, Position, Short Description, Pick, Throw, Runs, Overcount, Venue)
Cricket_Fielding_Analysis.xlsx - spreadsheet with the data, weights and a Performance Matrix using live formulas
cricket_fielding_analysis.py - calculates the scores, draws the charts and writes the report
charts/ - Performance Score, points breakdown, and runs saved or conceded by over
analysis_report.md - written analysis with strengths and areas to improve for each player

Run:

bash
cd Task3_Advanced
python cricket_fielding_analysis.py

Tools Used

Python, pandas, Matplotlib, Requests, Beautiful Soup, openpyxl, VS Code, Git and GitHub

Author

 NAME :- MOHD REHAN SIDDIQUI
 Email-id :- rehansiddiqui3393@gmail.com