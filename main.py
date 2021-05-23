from generator.main import generate_all
from db.utils import drop, backup, restore
from analysis import create_avarage_book_mark, create_worst_book_mark, create_best_book_mark, create_avarage_author_books_marks


def start_menu():
    print("\nSTART MENU")
    print("0. Exit.")
    print("1. Generate data")
    print("2. Drop data")
    print("3. Create Backup")
    print("4. Restore data")
    print("5. Analyze data")
    print("6. Replication")
    return int(input("Choose option: "))

def analysis_menu():
    print("\nANALYSIS MENU")
    print("0. Back.")
    print("1. Get average book rating from all resources")
    print("2. Get worst book rating from all resources")
    print("3. Get best book rating from all resources")
    print("4. Get average rating of the author's books")
    return int(input("Choose option: "))

def start():
    while True:
        action = start_menu()

        if action == 0:
            print("Exit...")
            break

        elif action == 1:
            generate_all(3, 3, 3)
            print("Data generated successfully!")

        elif action == 2:
            drop()
            print("Data dropped successfully!")

        elif action == 3:
            backup()
            print("Backup created successfully!")

        elif action == 4:
            restore()
            print("Data restored successfully!")

        elif action == 5:
            while True:
                analysis_action = analysis_menu()

                if analysis_action == 0:
                    print("Back...")
                    break

                elif analysis_action == 1:
                    create_avarage_book_mark()

                elif analysis_action == 2:
                    create_worst_book_mark()

                elif analysis_action == 3:
                    create_best_book_mark()

                elif analysis_action == 4:
                    author_name = input("Enter author name: ")
                    create_avarage_author_books_marks(author_name)
                else:
                    print("Unexpected option!")

        elif action == 4:
            restore()
            print("Data restored successfully!")

        else:
            print("Unexpected option!")


if __name__ == '__main__':
    start()
