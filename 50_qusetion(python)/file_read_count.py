filename = input("Enter filename: ")
try:
    with open(filename, 'r') as f:
        lines = f.readlines()
        words = sum(len(line.split()) for line in lines)
        print("Lines:", len(lines))
        print("Words:", words)
except FileNotFoundError:
    print("File not found.")