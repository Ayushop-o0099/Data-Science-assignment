class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

s1 = Student("Ayush", 101)
s1.display()