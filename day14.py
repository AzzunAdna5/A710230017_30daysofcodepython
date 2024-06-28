class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

# Creating an instance of the Person class
person = Person("Abdul Hakim", 25)

# Accessing and printing the initial values
print(person.get_name())  # Output: Abdul Hakim
print(person.get_age())   # Output: 25

# Setting new values using setter methods
person.set_name("Ryan Hakim")
person.set_age(30)

# Accessing and printing updated values
print(person.get_name())  # Output: Ryan Hakim
print(person.get_age())   # Output: 30

# Attempting to access __name directly will result in an AttributeError
# because __name is a private attribute (name mangling applied by Python)
# print(person.__name)  # This line will cause an AttributeError
