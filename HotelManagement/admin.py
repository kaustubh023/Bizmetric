from database import DatabaseConnection
from validations import Validate

class Admin:

    def add_menu(self):

        conn = None
        try:
            name =  Validate.correct_string(input("Enter Item Name: "))
            price =  Validate.correct_number(float(input("Enter Price: ")))

            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO menu (item_name, price) VALUES (?, ?)",
                (name, price)
            )
            conn.commit()

            print("Item Added Successfully")

        except Exception as e:
            print("Error:", e)

        finally:
            if conn:
                conn.close()


    def delete_menu(self):

        conn = None
        try:
            item_id = int(input("Enter Item ID to Delete: "))

            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM menu WHERE item_id = ?", (item_id,))
            conn.commit()

            print("Item Deleted Successfully")

        except Exception as e:
            print("Error:", e)

        finally:
            if conn:
                conn.close()
                
    def add_waiter(self):

        conn = None

        try:
            username =  Validate.correct_string(input("Enter Waiter Username: ").strip())
            password = input("Enter Password: ").strip()
            name = input("Enter Full Name: ").strip()
            salary = Validate.correct_number(float(input("Enter Salary: ")))
            work_days = int(input("Enter Work Days Per Year: "))

            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users (username, password, role, is_active) VALUES (?, ?, 'WAITER', 1)",
                (username, password)
            )
            conn.commit()

            cursor.execute("SELECT @@IDENTITY")
            user_id = cursor.fetchone()[0]

            cursor.execute(
                "INSERT INTO waiter (user_id, name, salary, work_days_per_year) VALUES (?, ?, ?, ?)",
                (user_id, name, salary, work_days)
            )
            conn.commit()

            print("Waiter Added Successfully!")

        except Exception as e:
            print("Error Adding Waiter:", e)

        finally:
            if conn:
                conn.close()



    def view_daily_revenue(self):

        conn = None
        try:
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT SUM(total_amount)
                FROM orders
                WHERE CAST(order_date AS DATE) = CAST(GETDATE() AS DATE)
            """)

            revenue = cursor.fetchone()[0]
            print("Today's Revenue:", revenue if revenue else 0)

        except Exception as e:
            print("Error:", e)

        finally:
            if conn:
                conn.close()
