class Menu:
    def __init__(self, title: str, options: dict, is_first_menu=False):
        self.title: str = title
        self.options: dict = options
        self.is_first_menu = is_first_menu

    def display(self):
        print(f"\n{self.title}")
        for key, value in self.options.items():
            print(f"{key}: {value}")
        if self.is_first_menu:
            print("q: Quit")
        else:
            print("b: Return to the previous menu")

    def get_choice(self):
        choice = input("Choose an option: ").strip().lower()
        if choice in self.options or (self.is_first_menu and choice == 'q') or (not self.is_first_menu and choice == 'b'):
            return choice
        else:
            print("Invalid choice. Please try again.")
            return self.get_choice()
