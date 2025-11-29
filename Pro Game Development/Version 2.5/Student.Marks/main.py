class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        pass

student1 = Student("Tim", [8.2, 9.1, 5.7, 6.7, 8.3, 7.2])
student2 = Student("Mike", [4.9, 5.6, 8.0, 7.7, 6.2, 5.9])

avg1 = student1.average()
avg2 = student2.average()

print(f"{student1[1]}'s average: {avg1}")
print(f"{student2[1]}'s average: {avg2}")

if avg1 > avg2:
    print(f"{student1} scored higher!")
elif avg1 < avg2:
    print(f"{student2} scored higher!")
else:
    print("Both students scored the same!!")
