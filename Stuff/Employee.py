class Employee:
    def __init__(self, employee_number, name, age, phone):
        self.employee_number = employee_number
        self.name = name
        self.age = age
        self.phone = phone
        self.role = 'Employee'

    def to_dict(self):
        return {
            'employee_number': self.employee_number,
            'name': self.name,
            'age': self.age,
            'phone': self.phone,
            'role': self.role
        }

    def __str__(self):
        return f"ID: {self.employee_number}, Name: {self.name}, Age: {self.age}, Phone: {self.phone}, Role: {self.role}"
