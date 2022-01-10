# Excel_Consolidate_macOS

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
