from database import DatabaseConnection

class User:

    def __init__(self, user_id, username, role):
        self.user_id = user_id
        self.username = username
        self.role = role

    @staticmethod
    def login():
        try:
            username = input("Enter Username: ").strip()
            password = input("Enter Password: ").strip()

            conn = DatabaseConnection.get_connection()
            cursor = conn.cursor()

            query = """
                    SELECT user_id, username, role
                    FROM users
                    WHERE username=? AND password=? AND is_active=1
                    """

            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            if user:
                print("\nLogin Successful!")
                return User(user[0], user[1], user[2])
            else:
                print("\nInvalid Credentials")
                return None

        except Exception as e:
            print("Login Error:", e)
            return None

        finally:
            if conn:
                conn.close()

    def logout(self):
        print(f"\n{self.username} logged out successfully.")
