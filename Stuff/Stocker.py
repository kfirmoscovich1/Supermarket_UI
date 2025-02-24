from Supermarket.Stuff.Employee import Employee

class Stocker(Employee):
    def __init__(self, employee_number, name, age, phone, attribute_1='Vest',attribute_2='Stock Cart'):
        super().__init__(employee_number, name, age, phone)
        self.role = 'Stocker'
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2

    def to_dict(self):
        return {
            'employee_number': self.employee_number,
            'name': self.name,
            'age': self.age,
            'phone': self.phone,
            'role': self.role,
            'attribute_1': self.attribute_1,
            'attribute_2': self.attribute_2
        }

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Phone: {self.phone}, Employee Number: {self.employee_number}, Role: {self.role}, attribute_1: {self.attribute_1}, attribute_2: {self.attribute_2}"
