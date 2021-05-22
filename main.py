from generator.main import generate_all
from db.utils import drop, backup, restore


def start_menu() -> int:
    print("\nSTART MENU", 15 * "-", ">")
    print("0. Exit.")
    print("1. Regression..")
    print("2. Regression..")
    print("3. ?\n")
    return int(input("Enter the number of action: "))


def start():
    while True:
        action = start_menu()

        if action == 0:
            print("Goodbye, have a good day :)")

        elif action == 1:
            generate_all(3, 3, 3)
            print("Data generated successfully!")

        elif action == 2:
            drop()
            print("Dropped database")

        elif action == 3:
            backup()
            print("Backup created successfully!")

        elif action == 4:
            restore()
            # todo

        else:
            print("Choose only available [0-3] actions :)")


if __name__ == '__main__':
    start()
