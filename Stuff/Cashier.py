from Supermarket.Stuff.Employee import Employee

class Cashier(Employee):
    def __init__(self, employee_number, name, age, phone, attribute_1='Standard Uniform', attribute_2='name tag'):
        super().__init__(employee_number, name, age, phone)

        self.role = 'Cashier'
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
        return f"ID: {self.employee_number}, Name: {self.name}, Age: {self.age}, Phone: {self.phone}, Role: {self.role}, attribute_1: {self.attribute_1}, attribute_2: {self.attribute_2}"
