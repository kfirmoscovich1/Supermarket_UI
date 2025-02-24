from Supermarket.Departments.Department import Department

class Deli(Department):
    def __init__(self, name: str = "Deli"):
        super().__init__(name)

    def department_info(self):
        return "This is the Deli Department."

    def __str__(self):
        return super().__str__()
