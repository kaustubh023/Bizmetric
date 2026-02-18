from user import User
from admin import Admin
from waiter import Waiter
from database import DatabaseConnection
from waiter import Waiter

def waiter_menu(user_id):

    conn = None

    try:
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT waiter_id FROM waiter WHERE user_id = ?",
            (user_id,)
        )
        result = cursor.fetchone()

        if not result:
            print("Waiter profile not found.")
            return

        waiter_id = result[0]

        waiter = Waiter(waiter_id)

        while True:
            print("\n1. View Menu")
            print("2. Take Order")
            print("3. View Profile")
            print("4. Logout")

            choice = input("Enter Choice: ")

            if choice == "1":
                waiter.view_menu()
            elif choice == "2":
                waiter.take_order()
            elif choice == "3":
                waiter.view_profile()
            elif choice == "4":
                break
            else:
                print("Invalid Choice")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            conn.close()



def admin_menu():

    admin = Admin()

    while True:
        print("\n1. Add Menu")
        print("2. Delete Menu")
        print("3. View Daily Revenue")
        print("4. Logout")
        print("4. Add Waiter")
        print("5. Logout")

        choice = input("Enter Choice: ")

        if choice == "1":
            admin.add_menu()
        elif choice == "2":
            admin.delete_menu()
        elif choice == "3":
            admin.view_daily_revenue()
        elif choice == "4":
            admin.add_waiter()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")


def waiter_menu(user_id):

    conn = None

    try:
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT waiter_id FROM waiter WHERE user_id = ?",
            (user_id,)
        )
        result = cursor.fetchone()

        if not result:
            print("Waiter profile not found.")
            return

        waiter_id = result[0]

        waiter = Waiter(waiter_id)

        while True:
            print("\n1. View Menu")
            print("2. Take Order")
            print("3. View Profile")
            print("4. Logout")

            choice = input("Enter Choice: ")

            if choice == "1":
                waiter.view_menu()
            elif choice == "2":
                waiter.take_order()
            elif choice == "3":
                waiter.view_profile()
            elif choice == "4":
                break
            else:
                print("Invalid Choice")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            conn.close()


def main():

    user = User.login()

    if not user:
        return

    if user.role == "ADMIN":
        admin_menu()
    elif user.role == "WAITER":
        waiter_menu(user.user_id)

    user.logout()


if __name__ == "__main__":
    main()
