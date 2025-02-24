class Person:
    def __init__(self, id_number, name, age, phone):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"ID: {self.id_number}, Name: {self.name}, Age: {self.age}, Phone: {self.phone}"
