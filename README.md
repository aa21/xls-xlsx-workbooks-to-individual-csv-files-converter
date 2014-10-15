xls-xlsx-workbooks-to-individual-csv-files-converter
====================================================

Convert all worksheets in xls &amp; xlsx files to individual csv files. 


Sample usage:

Find all XLS files and use the script on each file.
    find . -name '*.xls' -exec ./xlsx.py {}  \;


Find all XLS+XLSX files, don't recurse, use the script on each file, delete each XLS/XLSX file once done.
    find . -maxdepth 1  \( -name '*.xls' -o -name '*.xlsx' \) -exec ./xlsx.py {} \; -exec rm  {} \;
