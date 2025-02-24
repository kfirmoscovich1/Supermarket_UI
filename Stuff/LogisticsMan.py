from Supermarket.Stuff.Employee import Employee

class LogisticsMan(Employee):
    def __init__(self, id_number: str, name: str, age: int, phone_number: str, employee_number: str, hire_date: str, salary: float, logistics_area: str):
        super().__init__(id_number, name, age, phone_number, employee_number, hire_date, salary)
        self.logistics_area: str = logistics_area

    def manage_inventory(self):
        return f"{self.name} manages inventory in the {self.logistics_area} area."

    def work(self):
        return f"{self.name} works as a Logistics Man in the {self.logistics_area} area."

    def __str__(self):
        return (
            f"Logistics Man {self.name}, Age: {self.age}, Phone: {self.phone_number}, "
            f"ID: {self.id_number}, Employee Number: {self.employee_number}, Hire Date: {self.hire_date}, Salary: ${self.salary}, "
            f"Logistics Area: {self.logistics_area}"
        )

    def __eq__(self, other):
        if isinstance(other, LogisticsMan):
            return self.id_number == other.id_number
        return False
