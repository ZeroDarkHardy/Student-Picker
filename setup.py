from setuptools import setup

APP = ['student_picker.py']  # Your Python script
DATA_FILES = ['students.csv']  # Include the CSV file if needed
OPTIONS = {
    'argv_emulation': True,
    'includes': ['pandas'],  # Include libraries like pandas
    'packages': ['tkinter'],  # Include Tkinter explicitly
    'iconfile': 'app_icon.icns',  # Optional: Add a custom icon (.icns format)
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
