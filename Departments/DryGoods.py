from Supermarket.Departments.Department import Department

class DryGoods(Department):
    def __init__(self, name: str = "Dry Goods"):
        super().__init__(name)

    def department_info(self):
        return "This is the Dry Goods Department."

    def __str__(self):
        return super().__str__()
