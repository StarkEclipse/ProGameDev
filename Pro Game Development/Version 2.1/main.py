# Introduction to oop
# Object Oriented Programming Style

# Class: Blueprint
# Object: The thing you build from the blueprint

# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print(self.name, "says woof")

# pet1 = Pet("Kaeya", 2)
# pet2 = Pet("Bali", 3)

# pet1.speak()
# pet2.speak()

class Person:

    def __init__(self, name, age, height, hobbies):
        self.name = name
        self.age = age
        self.height = height
        self.hobbies = hobbies

    def greet(self):
        print(self.name, "says Hi")

person1 = Person("Onore", 16, 180, "Coding")
person2 = Person("Jah", 15, 178, "Gaming")
person3 = Person("Shano", 15, 174, "Basketball")

person1.greet()
person2.greet()
person3.greet()


