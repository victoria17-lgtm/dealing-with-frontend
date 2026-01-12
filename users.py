class Person:
    def _init_(self, age, name):
        self.name = name
        self.age = age

Person1 = Person(23, "Charles")
Person2 = Person(19, "Samuel")

print (Person1.age)