from Supermarket.Departments.Department import Department

class Butchery(Department):
    def __init__(self, name: str = "Butchery"):
        super().__init__(name)

    def department_info(self):
        return "This is the Butchery Department."

    def __str__(self):
        return super().__str__()
