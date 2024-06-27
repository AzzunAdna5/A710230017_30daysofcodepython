class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Position: {self.position}")


class Manager(Employee):
    def __init__(self, name, age, department):
        super().__init__(name, age, "Manager")
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


# Contoh penggunaan:
employee1 = Employee("John Doe", 30, "Software Developer")
employee1.display_info()

manager1 = Manager("Jane Smith", 35, "Engineering")
manager1.display_info()
