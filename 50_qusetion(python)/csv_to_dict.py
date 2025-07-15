import csv

filename = input("Enter CSV filename: ")
try:
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print(data)
except FileNotFoundError:
    print("File not found.")