# Excel_Consolidate
It's an automated program designed for the company's auto insurance division to help them with repetitive and time-consuming data extraction and management tasks.

By automating the program, they can save a week of raw data processing time per month.

## environment
- Python 3.9.5
- M1 maOS(ARM) / Microsoft Windows10 (x64)

## Introduction
Concat Excel files, merging and clean fields as needed, and retain necessary data.

## Processing steps

### grab_and_concat_files

Put the files to be consolidated in a specific path (consolidate_finder).
Use the xlrd engine to read excel files in Xls format, and combine multiple worksheets in a file into a DataFrame.
Process each Excel data that has been converted to a Dataframe, appending to the empty Dataframe created

### clean_unnecessary_data
Final cleanup of unnecessary data

### compile
Using Pyinstaller
- install
```python
pip3 install pyinstaller
```
- execute compilation
```python
# mac
pyinstaller -F ./hello.py

# windows
pyinstaller -F .\hello.py
```

### As a side note
If use a computer with Windows 7 version, you need to recompile the program in Python 3.8.6 version, 
otherwise may encounter the "api-ms-win-core-path-l1-1-0.dll" error message.
