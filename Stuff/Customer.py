from Supermarket.Stuff.Person import Person

class Customer(Person):
    def __init__(self, id_number: str, name: str, age: int, phone_number: str, membership: bool = False):
        super().__init__(id_number, name, age, phone_number)
        self.membership: bool = membership

    def shop(self):
        return f"{self.name} is shopping {'with membership' if self.membership else 'without membership'}."

    def __str__(self):
        return (
            f"Customer {self.name}, Age: {self.age}, Phone: {self.phone_number}, "
            f"ID: {self.id_number}, Membership: {'Yes' if self.membership else 'No'}"
        )

    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.id_number == other.id_number
        return False
