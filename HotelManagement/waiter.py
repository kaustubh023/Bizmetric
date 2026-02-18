from database import DatabaseConnection

class Waiter:

    def __init__(self, waiter_id):
        self.waiter_id = waiter_id


    def view_menu(self):

        conn = None
        try:
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM menu")
            rows = cursor.fetchall()

            print("\n----- MENU -----")
            for row in rows:
                print(f"{row[0]} | {row[1]} | ₹{row[2]}")

        except Exception as e:
            print("Error:", e)

        finally:
            if conn:
                conn.close()


    def take_order(self):

        conn = None
        try:
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()

            total = 0
            items = []

            while True:

                item_name = input("Enter Item Name : ")
                qty = int(input("Enter Quantity: "))

                cursor.execute("SELECT price FROM menu WHERE item_name = ?", (item_name,))
                result = cursor.fetchone()

                if not result:
                    print("Item Not Found")
                    continue

                price = result[0]
                subtotal = price * qty
                total += subtotal

                items.append((item_name, qty, subtotal))

                more = input("Add more items? (y/n): ")
                if more.lower() != 'y':
                    break

            cursor.execute(
                "INSERT INTO orders (waiter_id, total_amount) VALUES (?, ?)",
                (self.waiter_id, total)
            )
            conn.commit()

            cursor.execute("SELECT @@IDENTITY")
            order_id = cursor.fetchone()[0]

            for item in items:
                cursor.execute(
                    "INSERT INTO order_details (order_id, item_id, quantity, subtotal) VALUES (?, ?, ?, ?)",
                    (order_id, item[0], item[1], item[2])
                )

            conn.commit()

            print("\n======= BILL =======")
            print("Order ID:", order_id)
            print("Total Amount: ₹", total)
            print("====================")

        except Exception as e:
            print("Order Error:", e)

        finally:
            if conn:
                conn.close()


    def view_profile(self):

        conn = None
        try:
            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM waiter WHERE waiter_id = ?", (self.waiter_id,))
            waiter = cursor.fetchone()

            if waiter:
                print("\n---- Profile ----")
                print("ID:", waiter[0])
                print("Name:", waiter[2])
                print("Salary:", waiter[3])
                print("Work Days:", waiter[4])

        except Exception as e:
            print("Error:", e)

        finally:
            if conn:
                conn.close()
