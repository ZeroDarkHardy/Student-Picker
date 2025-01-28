# Student Picker
Created by Matt Hardy, 2025

An interactive, dynamic tool for instructors to randomly select students from a list, ensuring fairness and tracking answered students. Built with Python and styled for a professional look, this application is perfect for classrooms and bootcamps.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage Instructions](#usage-instructions)
  - [For PC](#for-pc)
  - [For macOS](#for-macos)
  - [Running the Python File](#running-the-python-file)
- [CSV File Format](#csv-file-format)

---

## Features

- Random student selection with fairness: no repeats until all students have answered.
- Tracks answered students and displays uplifting messages for each.
- Scrollable "Answered Students" list with auto-scroll.
- Restart queue automatically when all students have answered.
- Dynamic resizing and styled interface.
- macOS version is a standalone app, while PC requires an external CSV file.

---

## Installation

### Requirements
- Python 3.8 or higher (for source code execution).
- Pre-built executables are available for both PC and macOS.

### Pre-Built Executables
- Download the appropriate executable for your system from the repository's [Releases](https://github.com/ZeroDarkHardy/Student-Picker/releases).

---

## Usage Instructions

### For PC
1. Download the executable from the [Releases](https://github.com/ZeroDarkHardy/Student-Picker/releases).
2. Place the `students.csv` file in the same directory as the executable.
3. Double-click the executable to run the program.

### For macOS
1. Download the `.app` file from the [Releases](https://github.com/ZeroDarkHardy/Student-Picker/releases).
2. Drag and drop the app into your `Applications` folder.
3. On the first run, you may encounter a security warning stating the app cannot be opened because it is from an unidentified developer.
4. To unblock the app:
   - Open **System Preferences**.
   - Go to **Security & Privacy**.
   - Under the **General** tab, you will see a message about the app being blocked. Click **Open Anyway**.
   - Confirm by clicking **Open** in the pop-up window.
5. After unblocking, double-click the app to run. No additional files are needed.

### Running the Python File
1. Ensure Python 3.8 or higher is installed on your system.
2. Install the required dependencies by running:
   ```bash
   pip install tkinter
   ```
   (Note: `tkinter` is pre-installed with most Python distributions, but ensure it's available.)
3. Place the `students.csv` file in the same directory as `student_picker.py`.
4. Run the script by executing:
   ```bash
   python student_picker.py
   ```
5. The application will launch and function as described.

---

## CSV File Format

The `students.csv` file must contain a list of student names in the following format (no header row):

```
Doe,John
Smith,Jane
Johnson,Alex
Brown,Samantha
```

Ensure the file is saved in UTF-8 encoding and placed alongside the executable (for PC) or the script (if running directly).

