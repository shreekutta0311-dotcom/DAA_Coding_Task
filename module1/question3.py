##Read a csv file of student data, search for the names that contain characters 'ai' and return the cell numbers.
import csv

file = open('students.csv', 'r') 
read = csv.read(file)

rowindex = 0
for row in read:
    columnindex = 0
    while columnindex < len(row):
        cell = row[columnindex]
        if 'ai' in cell.lower():
            print("Match at Row", rowindex + 1, "Column", columnindex + 1, ":", cell)
        columnindex += 1
    rowindex += 1

file.close()

