from Supermarket.Departments.Department import Department

class GreenGrocer(Department):
    def __init__(self, name: str = "Green Grocer"):
        super().__init__(name)

    def department_info(self):
        return "This is the Green Grocer Department."

    def __str__(self):
        return super().__str__()
