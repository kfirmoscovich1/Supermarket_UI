import sys
from Supermarket.UI.ConsoleUI import ConsoleUI

def main():
    console_ui = ConsoleUI()
    try:
        console_ui.show_menu()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
